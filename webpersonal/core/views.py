from django.shortcuts import render, HttpResponse #HttpResponse me permite responder a una peticion devolviendo un código

# html_base = """
# <h1>Mi web - prueba</h1><h2>Portada</h2>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/aboutme">Acerca de</a></li>
#     <li><a href="/portfolio">Portafolio</a></li>
#     <li><a href="/contacto">Contacto</a></li>
# </ul>    
# """

# Create your views here.
# #Una forma
# def home(request):
#      #html_response = "<h1>Mi web - prueba</h1>"
#      #for x in range(3):
#       #  html_response +="<h2>Portada</h2>"
#     #return HttpResponse("<h1>Mi web - prueba</h1><h2>Portada</h2>")
#     return HttpResponse(html_base + """
#         <h2>Portada</h2>
#         <p>Esto es la portada</p>
#         """)

#Otra forma
def home(request):
    return render(request, "core/home.html") #le paso la vista que esta en el directorio core

# def about(request):
#     return HttpResponse(html_base + """
#     <h2>Acerca de </h2>
#     <p>Vamos a bailaaaar, algo que esta perrón que toda la gente grita de emoción</p>
#     """)
def about(request):
    return render(request, "core/about.html")

# def porfolio(request):
#     return HttpResponse(html_base + """
#     <h2>Portafolio </h2>
#     <p>Trabajos</p>
#     """)   

""" def portfolio(request):
    return render(request, "core/portafolio.html") """

# def contacto(request):
#     return HttpResponse(html_base + """
#     <h2>Contacto </h2>
#     <p>Celulares y esas vainas</p>
#     """)    

def contacto(request):
   return render(request, "core/contact.html")  

