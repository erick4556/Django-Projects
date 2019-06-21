"""webempresa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from core import views ya no la voy a usar por que lo voy hacer en el mismo core

from django.conf import settings

urlpatterns = [
    #Path del core
    #Otra forma para las rutas
    path('', include('core.urls')),
    path('blog/', include('blog.urls')),
    path('page/', include('pages.urls')),
    path('contact/', include('contact.urls')),
    path('services/', include('services.urls')),

    #Path del admin
    path('admin/', admin.site.urls),
]

if settings.DEBUG: #solo va funcionar si esta en modo debug
    from django.conf.urls.static import static #ayuda a servir ficheros estáticos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Le paso el MEDIA_URL y el document_root, la raíz donde tiene que ir a buscar los ficheros media 
