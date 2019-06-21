from django.contrib import admin
from .models import Proyecto

# Register your models here.
#Esta clase es para extender las funcionalidades del panel de admin
class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Redifino los campos que son de solo lectura para que lo muestre en el campo del panel


#admin.site.register(Proyecto)
admin.site.register(Proyecto, ProyectoAdmin) #ProyectoAdmin es parte de la configuración extendida para que salga el campo created y updated