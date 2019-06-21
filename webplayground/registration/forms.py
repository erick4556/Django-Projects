from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido perro, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ("username","email","password1","password2") #Esto funciona por que email ya es un campo dentro del User, yo solo le añado un field al formulario que ya existe dentro del modelo User
        #y le digo que lo use, si no existiera ese campo dentro del modelo no funcionaría

    #Para la validación del correo
    def clean_email(self): #Tiene que ser clean y relacionado con algunos de los campos        
        email = self.cleaned_data.get("email") #Recupero el email que voy a validar
        if User.objects.filter(email=email).exists(): #Compruebo si existe un usuario con este email que recibo
            raise forms.ValidationError("El email ya existe perro, prueba con otro") #Esto aparecerá en el formulario
        return email #En caso de que no se encuentre ningun usuario con este email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio' : forms.Textarea(attrs={'class':'form-control mt-3','rows':3, 'placeholder':'Biografía'}),
            'link' : forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

#Para editar el email
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido perro, 254 caracteres como máximo y debe ser válido")
    class Meta:
        model = User
        fields = ['email']
    #Para la validación del correo
    def clean_email(self): #Tiene que ser clean y relacionado con algunos de los campos        
        email = self.cleaned_data.get("email") #Recupero el email que voy a validar
        if 'email' in self.changed_data: #Comprobar si el campo email esta dentro de self.changed_data que es una lista que almacena todos los campos que se han editado en el formulario
            #Si esta dentro se ha modificado, por eso hago la otra comprobación, solo dejo guardar el email si no lo tiene ningun usuario antes
            if User.objects.filter(email=email).exists(): #Compruebo si existe un usuario con este email que recibo
                raise forms.ValidationError("El email ya existe perro, prueba con otro") #Esto aparecerá en el formulario
        return email #En caso de que no se encuentre ningun usuario con este email   