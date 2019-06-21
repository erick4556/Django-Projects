from django.shortcuts import render
from django.views.generic.base import TemplateView

#Vista basada en clases
class HomePageView(TemplateView):
    template_name = "core/home.html"

    """   #Sobreescribir el diccionario de contexto
    def get_context_data(self, **kwargs): #Recibe el self, y unos argumentos en clave y valor que se pasa con 2 asterisco
        context = super().get_context_data(**kwargs)#Recupera el diccionario de contexto
        context['title'] = "Super Web Playground" #Definir algun valor que queramos
        return context """
   # return render(request, template_name)

    #def get(self,request): No se recomienda dejarlo asi por defecto
    #Casi siempre que se este sobreescribiendo métodos dentro de una vista basada en clase se estará pasando los argumentos o los argumentos en clave y valor o los dos.
    def get(self,request, *args, **kwargs): #Es buena practica importar sus argumentos y sus argumentos en clave y valor 
       return render(request,self.template_name,{'title':"Super Web Playground"}) #Se pasa el diccionario de contexto con su clave y valor
    

#def home(request):
#    return render(request, "core/home.html")

class SamplePageView(TemplateView):
    template_name = "core/sample.html"

""" def sample(request):
    return render(request, "core/sample.html") """