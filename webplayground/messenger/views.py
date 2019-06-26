from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread, Message
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your views here.
@method_decorator(login_required,name="dispatch") #Para ver si esta logueado
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"


  #  No voy a necesitar esto de abajo, por que en el template puedo consultar todos los hilos del usuario

    """  model = Thread 
    #Filtrar un queryset por defecto
    def get_queryset(self):
        queryset = super(ThreadList,self).get_queryset() #Recupero el queryset. Aqui tengo todas instancias de thread
        return queryset.filte(user=self.request.user) #Filtro por el usuario qeu esta identificado """


@method_decorator(login_required,name="dispatch") #Para ver si esta logueado
class ThreadDetail(DetailView):
    model = Thread

    #Para que usuario pueda ver los hilos de los que forma parte
    #Sobreescribo el método get_object
    def get_object(self):
        obj = super(ThreadDetail,self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404() #Invocar un error
        return obj

def add_message(request, pk):
    #print(request.GET)
    json_response = {'created':False} #Respuesta que voy a devolver
    if request.user.is_authenticated: #Para ver si hay un usuario autenticado
        content = request.GET.get('content',None) #Recuperar el contenido. get('content',None) este get tiene los diccionarios, puedo recuperar la clave content y si no existe None
        if content:
            thread = get_object_or_404(Thread, pk=pk)  #Recuperar el hilo, y paso la pk que le pasé a la vista
            message = Message.objects.create(user=request.user, content=content) #Crea un mensaje con el usuario request.user que esta identificado 
            thread.messages.add(message)#Añadir al hilo el mensaje
            json_response['created'] = True #Cambiar el valor diccionario json a True
            if len(thread.messages.all()) is 1: #Si la longitud tiene un mensaje y solo 1 en la conversación
                json_response['first'] = True
    else:
        raise Http404("Usuario no autenticado") #Devuelvo un error    
    return JsonResponse(json_response) #Automaticamente hace la conversión del diccionaro de python a un objeto json   

@login_required #Para ver si el usuario esta identificado. No le agredo el adorno al método por que es una vista comun y corriente
def start_thread(request,username): #Paso el username con el que quiero empezar a hablar
    user = get_object_or_404(User,username=username)
    thread = Thread.objects.find_or_create(user, request.user) #Creo el hilo. Uso el método que buscaría o devuelve el hilo si ya existe, luego creo el hilo con los parametros que le paso
    return redirect(reverse_lazy('messenger:detail',args=[thread.pk])) #Le envío al hilo los argumentos con args que va una lista y el primero es thread.pk