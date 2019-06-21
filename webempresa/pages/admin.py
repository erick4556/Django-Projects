from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Redifino los campos que son de solo lectura para que lo muestre en el campo del panel
    list_display = ('title', 'order') #Añado una tupla que muestre un título y el campo de ordenación order


admin.site.register(Page,PageAdmin)

