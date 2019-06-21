from django.shortcuts import render
from .models import Proyecto

# Create your views here.
def portfolio(request):
    #Recupera la lista de proyecto que tengo almacenado gracias al ORM de django
    projects = Proyecto.objects.all()#devuelve todos los objetos que tiene el modelo
    return render(request, "portfolio/portafolio.html",{'projects':projects})