from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
class ThreadDetail(ListView):
    model = Thread

    #Para que usuario pueda ver los hilos de los que forma parte
    #Sobreescribo el método get_object
    def get_object(self):
        obj = super(ThreadDetail,self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404() #Invocar un error
        return obj
