from django import template
from pages.models import Page

register = template.Library() #Guardo la referencia a la librearia de template.Library() 


@register.simple_tag #Decorador a la función, para implementar una nueva funcionalidad
def get_page_list():
    pages = Page.objects.all()
    return pages
#Lo que hice fue que transformé una función normal en un tag simple y lo registro en la librearia de template..... Ojo hay que reiniciar el servidor para que incluya los nuevos template_tags en la memoria
   