from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 3 #Para paginación

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    #Recupero el objeto
    #Como lo estoy pasando a partir del username en el path, sobreescribo esta función y ya no lo puedo dejar solo por que se tienen que pasar datos forma de pk o slug
    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username']) #Filtro a partir del campo username del User, pasando como argumento self.kwargs['username'] que hace referencia en las url
