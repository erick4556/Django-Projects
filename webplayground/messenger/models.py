from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed #Señal

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #Si se borra el usuario de la base de datos se borra tambien todos sus mensajes
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['created']

#Crear un objectManage TDD(3)
class ThreadManager(models.Manager):
    def find(self,user1,user2):
        #self #El self sería igual a Thread.objects.all
        queryset = self.filter(users=user1).filter(users=user2)
        if len(queryset)>0:#Si la longitud es mayor a 0 entonces hay un hilo
            return queryset[0] #Le paso el que tengo en la primera posisión
        return None    

    def find_or_create(self,user1,user2):
        thread = self.find(user1,user2)#Ver si el hilo existe
        if thread is None: #Si no hay un hilo lo creo 
            thread = Thread.objects.create()
            thread.users.add(user1,user2)
        return thread 

class Thread(models.Model):
    users = models.ManyToManyField(User,related_name='threads') #Uso el related_name para poder acceder desde un user, haciendo user.threads, búsqueda inversa, todo los hilos a los que pertenece
    messages = models.ManyToManyField(Message) #Almacena todos los mensajes que forman parte del hilo

    #TDD(3)
    objects = ThreadManager() #A mi hilo asigno el objects ThreadManager() para poder crear filtros personalizados

def messages_changed(sender, **kwargs):
    #Recuperación
    instance = kwargs.pop("instance",None) #Instancia que esta mandando la señal, hilo al que intento añadir los mensajes
    action = kwargs.pop("action", None)#La acción que se esta ejecutando, ya que la señal tiene varias acciones, preadd o postadd, pero quiero detectar el preadd
    pk_set = kwargs.pop("pk_set",None)#Hace referencia a un conjunto que almacena los id de todos los mensajes que se van añadir dentro de la relación ManytoMany
    print(instance,action,pk_set) 

    false_pk_set = set()
    if action is "pre_add": #Comprobar antes de que se añade
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk) #Recupero los mensajes
            if msg.user not in instance.users.all(): #Si el autor del mensaje no se encuentra dentro de los usuarios que hay añadidos en la instancia del hilo
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk) #Almaceno aqui los mensajes fraudalentos

    #Buscar los mensajes de false_pk_set que si están en pk_set y los borro del pk_set
    pk_set.difference_update(false_pk_set)                 

m2m_changed.connect(messages_changed, sender=Thread.messages.through) #Me conecto a la señal con cualquier cambio que suceda en el campo messages .messages_changed la señal que quiero conectar.   

