from django.urls import path
#from . import views
from .views import HomePageView, SamplePageView #Importo la vista para la portada y la vista de la página sample

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
]