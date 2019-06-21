from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    #Para hacer responsivo el campo del text área   
    # Inyectamos nuestro fichero css
    class Media:
        css = { #Sobreescribo un diccionario css
            'all': ('pages/css/custom_ckeditor.css',) #En la clave all importo con una tupla el css que he creado....
        }

admin.site.register(Page, PageAdmin)
