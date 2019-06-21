from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Redifino los campos que son de solo lectura para que lo muestre en el campo del panel

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists(): #Comprueba si dentro del grupo personal existe el usuario
            return ('created','updated','key','name') #El readonly_fields va tener el varlo de esta tupla
        else:    
            return ('created','updated') #Sino solo lectura va ser created and updated como siempre

admin.site.register(Link,LinkAdmin) #LinkAdmin es parte de la configuración extendida para que salga el campo created y updated

