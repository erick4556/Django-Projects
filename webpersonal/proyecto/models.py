from django.db import models

# Create your models here.
class Proyecto(models.Model): #herede Model de models, esta clase representa una tabla de la base de datos
    #columnas
    title = models.CharField(max_length=200,verbose_name="Titulo")#Y asi puedo agregar el verbose_name en los demas campos para la traducción
    description = models.TextField()
    image = models.ImageField(upload_to="projects")#upload_to para decir donde quiero que se suban las imagénes media y en este caso lo hagan en el directorio proyecto
    link = models.URLField(verbose_name="Dirección web",null=True, blank=True)#null y blank por que el campo es opcional
    created = models.DateTimeField(auto_now_add=True) #el auto_now_add es para que ponga la hora cuando se crea la primera vez
    updated = models.DateTimeField(auto_now=True) #igual, solo que se ejecuta cada vez que se actualiza una instancia

    #Para que django detecte el nombre en español del modelo
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #ordenar los campos, se pueden ordernar por varios campos a la vez, pero lo voy a hacer por creación. Ordeno de más nuevos a antiguos para eso uso - antes del campo

    def __str__(self):
        return self.title #Me devuelva el nombre del proyecto cuando listo los proyecto y no me salga Proyecto objetc(1)  