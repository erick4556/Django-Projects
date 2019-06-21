from django.urls import path
from . import views

urlpatterns = [
     path('<int:page_id>/<slug:page_slug>/', views.page, name="page") #int: cambia el tipo de dato y recoge un número entero, que me sirve para filtrar 

]    