from django.shortcuts import render, get_object_or_404
from .models import Page

# Create your views here.
def page(request, page_id, page_slug):#Ese page_id es el identificador de la página
    page = get_object_or_404(Page, id=page_id)#Recupero la página haciendo el get_object_or_404, pasandole el modelo page y por lo que tiene que encontrarlo o filtrarlo que es page_id 
    return render(request, 'pages/sample.html',{'page':page})

