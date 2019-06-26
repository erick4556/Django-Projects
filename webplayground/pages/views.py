from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy #Ese reverse_lazy es para peresosos
from .forms import PageForm #Cargo de form el formulario que acabo de crear
from django.contrib.admin.views.decorators import staff_member_required #Importo decorador para seguridad
from django.utils.decorators import method_decorator #Importo decorador de métodos

""" #Para hacer el Mixin
class StaffRequiredMixin(object): #Heredo object que es la clase base de todas las clases de python
    #Este mixin requiere que el usuario sea miembro del staff

     #Para seguridad los métodos update, create y delete. Sobreescribo el método dispatch
    def dispatch(self, request, *args, **kwargs):
       #print(request.user)
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login')) #Si no tienes permiso del staff te jodiste perro, mueve para el login
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) """

#Para hacer el Mixin y usando decoradores
class StaffRequiredMixin(object): #Heredo object que es la clase base de todas las clases de python
    #Este mixin requiere que el usuario sea miembro del staff

     #Para seguridad los métodos update, create y delete. Sobreescribo el método dispatch y uso un decorador
    @method_decorator(staff_member_required) #Le paso al decorador el staff_member_required, y añade el requisito que tiene que ser miembro del staff al método dispatch 
    def dispatch(self, request, *args, **kwargs):
        #Ojo no hago las desiciones por que el decorador hace eso.
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)         


# Create your views here.
#Vistas basadas en clases
class PagesListView(ListView):#Cuando voy a la página me tirar error si no coloco un template como django lo pide por ejemplo page_list, nombre del modelo page barra abajo list
    model = Page #Le digo que tiene que gestionar el modelo Page

class PageDetailView(DetailView):#Cuando voy a la página me tirar error si no coloco un template como django lo pide por ejemplo page_detail, nombre del modelo page barra abajo detail
    model = Page

#Con formulario incluido.
#class PageCreate(StaffRequiredMixin,CreateView): #Le doy prioridad a StaffRequiredMixin que es para la seguridad, por eso lo pongo a la izquierda.
@method_decorator(staff_member_required, name='dispatch')#Uso el decorador en la vista basada en clase y como no es un método sino una clase le paso un parámetro name='dispatch', osea que decore el dispatch
class PageCreate(CreateView): #Ahora no uso el Mixin, sino el decorador, hace lo mismo que el Mixin en una sola línea
    model = Page
    form_class = PageForm #Viene del fichero forms
    success_url = reverse_lazy('pages')


""" class PageCreate(CreateView):
    model = Page
    fields = ['title','content','order']
    success_url = reverse_lazy('pages') """

#Lo comento por que voy a usar un método menos largo que es el reverse_lazy
#    def get_success_url(self): #Sobreescribo este método  
#         return reverse('pages') #Para que vaye a buscar de forma correcta la página y me deje ingresar los datos por el formulario
#         #return reverse('pages:pages') Si me funcionara la forma de ruta diferente pero no funciona un carajo...

@method_decorator(staff_member_required, name='dispatch')
#class PageUpdate(StaffRequiredMixin,UpdateView):
class PageUpdate(UpdateView):
    model = Page
    #fields = ['title','content','order']
    form_class = PageForm
    template_name_suffix = '_update_form' #Esto es para usar otro formulario y no agarre el mismo del create
    
    #Para que despues que se actualice me mande al mismo formulario
    def get_success_url(self):
        return reverse_lazy('update', args=[self.object.id]) + '?ok' #args = argumentos

class PageDelete(StaffRequiredMixin,DeleteView):
    model = Page
    success_url = reverse_lazy('pages')        


#Forma tradicional
""" def pages(request):
    pages = get_list_or_404(Page)
    return render(request, 'pages/pages.html', {'pages':pages})

def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page}) """