from django.contrib import admin
from .models import Category,Post
# Register your models here.
#Esta clase es para extender las funcionalidades del panel de admin
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Redifino los campos que son de solo lectura para que lo muestre en el campo del panel

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Redifino los campos que son de solo lectura para que lo muestre en el campo del panel    
    list_display = ('title','author', 'published','post_categories') #Muestre solo los campos que quiero, para las categorias tengo que usar el método de abajo, no solo pongo categories por que no es un campo que se pueda mostrar en una columna 
    ordering = ('author','published') #Para ordernar por campos, si quiero solo uno, tengo que dejarlo con una coma después
    search_fields = ('title','content','author__username','categories__name')#Para poner el buscador, si lo quiero buscar por autor, le digo que de author busque username, por que es un campo foranéo
    #igual lo hago con categorias, hago referencia al nombre de la categoria
    date_hierarchy = 'published' #Muestra los campos por fechas
    list_filter = ('author__username','categories__name') #Agregar filtro, agrego que filtre por los usuarios  o lo que quiera.

    #Método para listar las categorias, ya que hay una relación many to many
    def post_categories(self,obj): #obj por que hara referencia a cada fila que se muestre
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    #Agregarle un campo a esa columna
    post_categories.short_description = "categorias-Perro"


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

