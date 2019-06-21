from django.urls import path
from . import views

urlpatterns = [
     path('', views.blog, name="blog"),
     path('category/<int:category_id>/', views.category, name="category") #int: cambia el tipo de dato y recoge un número entero, que me sirve para filtrar 

]    