from django import forms #Importo la libreria forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required =True, widget=forms.TextInput(#Uso el atributo label, por que label crea dentro del html cuando se genere el formulario un tag label y dentro pone el nombre del campo
        #Voy a buscar un textinput de form y le paso unos atributos
        attrs={'class':'form-control','placeholder':'Escribe tu nombre'} #attrs es un diccionario, de una vez me lo paso al html al input name
    ), min_length=3, max_length=8) 
    #El widget que estoy utilizando al final del campo, es para extender la configuración del input
    email = forms.EmailField(label="Email",required = True,widget=forms.EmailInput(
         attrs={'class':'form-control','placeholder':'Escribe tu email'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido",required= True, widget=forms.Textarea(
        attrs={'class':'form-control','rows':3,'placeholder':'Escribe tu mensaje'} #Hago otra clave llamada rows y que sea de 3 filas, y asi puedo agregar otras claves
    ), min_length=10, max_length=1000) #widget le digo que sea un textarea
