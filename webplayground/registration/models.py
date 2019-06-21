from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #Importo este decorador
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):#instance hace referencia al objeto que se esta guardando, filename nombre del fichero con la imagen a sobreescribir
    old_instance = Profile.objects.get(pk=instance.pk) #Recupero la instancia justo como estaba antes de guardarla
    old_instance.avatar.delete() #La borro
    return 'profiles/'+filename #Le indico que tiene que guardar el fichero en profiles con su nombre 
#Ojo si hay dos imágenes iguales, la segunda la modifica


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Para que cuando se borre el usuario también se borre su perfil. OneToOne indica al modelo que solo puede haber un perfil por cada usuario, no se pueden tener dos perfiles
    #para un usuario ni distintos usuarios para un perfil
    #avatar =  models.ImageField(upload_to='profiles', null=True, blank=True)
    avatar =  models.ImageField(upload_to=custom_upload_to, null=True, blank=True) #Agrego la función que he creado arriba
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    #Esto lo voy hacer para ordenar en la paginación
    class Meta:
        ordering = ['user__username'] #Ordena a partir del nombre del usuario


#Crear el perfil automaticamente
@receiver(post_save, sender=User)#Le paso la señal post_save y el cual es el modelo que tiene que enviar la señal
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False): #Si dentro de kwargs existe una clave created, si existe significa que es la primera vez que se guarda la instancia. Devuelvo por defecto False si no existe esa entrada created en el diccionario
        Profile.objects.get_or_create(user=instance)#Crea una instancia de perfil si no existe
        #print("Se acaba de crear un usuario y su perfil enlazado") #Mensaje cuando hago el test
