from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #Importo el modelo de usuario

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = "Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name   

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)#El default es para que ponga la fecha y hora en la que se creo esa entrada.
    image = models.ImageField(verbose_name="Imagen",upload_to="", null=True, blank=True)#El upload_to le asigno un directorio, y le digo que puede ser nullo o en blanco.
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)#Con el User enlazo un usuario como si fuera el autor de cada entrada, el ondelete para borrar todas las entradas que tenía ese autor
    #categories = models.ManyToManyField(Category, verbose_name="Categorías")#Hago referencia a la categoria que tengo arriba 
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")#get_posts es un accesor ya que tiene más sentido que ese post_set que puse - Asi que definiendo ese related_name yo puedo buscar
    #la relación inversamente a partir de ese campo como si fuera otro campo más del modelo principal, ahora puedo crear con el related_name otros campos relacionados entre la categoría y un post, irlos a buscar inversamente de la forma que yo quiero.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")      

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title   