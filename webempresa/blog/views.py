from django.shortcuts import render, get_object_or_404 #Este último método para manejar los errores
from .models import Post,Category

# Create your views here.

def blog(request):
    posts = Post.objects.all() #Recupero todos los mensajes
    return render(request, "blog.html",{'posts':posts})

def category(request, category_id):
     #category = Category.objects.get(id=category_id) #Encuentre la categoria con ese id
     category = get_object_or_404(Category,id=category_id) #Paso el modelo y encuentre la categoria con ese id
    # posts = Post.objects.filter(categories=category)
    # return render(request, "category.html",{'category':category,'posts':posts})   
     return render(request, "category.html",{'category':category}) 
