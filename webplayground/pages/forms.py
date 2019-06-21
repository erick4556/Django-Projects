from django import forms #importo la estructura de los campos. 
from .models import Page #Voy a enlazar el modelo para que se genere automaticamente y no lo tenga que crear desde cero

#Crear el modelo del formulario
class PageForm(forms.ModelForm):

    class Meta:
        model = Page #Enlazo el modelo page como hacia en las vistas basadas en clases
        fields = ['title','content','order'] #Le digo que campos puedo editar o crear en el formulario
        #Creo un diccionario
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder' : 'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control','placeholder' : 'Orden'}),
        }

        labels = {
            'title':'',
            'order':''
        } 
       

 