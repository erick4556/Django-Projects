from django.urls import path
from . import views #El . significa que importo del directorio actual

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    #path('services/',views.services, name="services"),
    path('store/',views.store, name="store"),
    #path('contact/',views.conctact, name="contact"),
    #path('blog/',views.blog, name="blog"),
    
]
