from django.urls import path
from .views import PagesListView, PageDetailView, PageCreate, PageUpdate, PageDelete #Para el nuevo método

pages_patterns = [
   # path('', views.pages, name='pages'),
   path('', PagesListView.as_view(), name='pages'),
   # path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
   path('<int:pk>/<slug:page_slug>/', PageDetailView.as_view(), name='page'), #En luga de ponerle page_id, le digo que es pk por que es lo que server esta esperando, tambien acepta uno que se llame
   #slug en ves de page_slug pero como no estoy almacenando un slug dentro de la base de datos lo puedo dejar así.
   path('create/',PageCreate.as_view(), name="create"),
   path('update/<int:pk>',PageUpdate.as_view(), name="update"),
   path('deleteperro/<int:pk>',PageDelete.as_view(), name="delete"),
]