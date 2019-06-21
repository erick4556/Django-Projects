#from django.contrib.auth.forms import UserCreationForm Ya no lo importo de aquí sino del forms customizado que he hecho
from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms #Para acceder a los widgets
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required #Para que pida que este logueado
from .models import Profile

# Create your views here.
class SignUpView(CreateView): #Vista basada en clases
   # form_class = UserCreationForm #El formulario que tiene que mostrar en la vista 
   form_class = UserCreationFormWithEmail #El formulario que tiene que mostrar en la vista 
   # success_url = reverse_lazy('login') #Redireccione al login después que hago el registro
   template_name = 'registration/signup.html' #Para que cargue el template que voy a tener cargado en registration

   def get_success_url(self):
        return reverse_lazy('login') + '?register' #args = argumentos

   def get_form(self, form_class=None):#Le paso por defecto un form_class=None
        form = super(SignUpView, self).get_form() #Recupero al formulario, asignando a form la llamada superclase de SignUpView. El get_form() es como si ejecutara la propia función, me devuelve el formulario
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
     form_class = ProfileForm #Como el modelo viene del ProfileForm ya no tengo que poner mode = modelo
     success_url = reverse_lazy('profile')
     #template_name = 'registration/profile_form.html'

     #Recuperar el id para editarlo
     def get_object(self): #Voy a sobreescribir este método
          #recuperar el objeto que se va editar
          profile, create = Profile.objects.get_or_create(user=self.request.user) 
          return profile
          #get_or_create: Lo que hace es conseguir o crear, busca a partir del filtro que le doy y si no lo encuentra lo crea. Lo malo es que no puedo recuperarlo y devolverlo directamente por que devuelve una tupla
          #formada por el objeto que recupero o edito y una variable de tipo boleano que dice si se almacenó o no.

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
     form_class = EmailForm #Como el modelo viene del ProfileForm ya no tengo que ponerlo
     success_url = reverse_lazy('profile')
     template_name = 'registration/profile_email_form.html'

     #Recuperar el id para editarlo
     def get_object(self): #Voy a sobreescribir este método
          #Recuperar el objeto que se va editar
          return self.request.user #Recupero el usuario

     #Sobreescribir el formulario, uso la función get_form
     #Sobreescribo el widget en tiempo de ejecución por que el modelo de usuario ya tiene sus propios validadores y widgets
     def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form() #Recupero al formulario, asignando a form la llamada superclase de SignUpView. El get_form() es como si ejecutara la propia función, me devuelve el formulario
        #Modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Email'})
        return form      
         