from .models import Link

#Esta función es para decir que voy a extender el diccionario de contexto
def ctx_dict(request):
    #ctx = {'test':'hola'} #diccionario de contexto de prueba con una clave test y un valor
    ctx = {}#El diccionario va vacío perro
    links = Link.objects.all()
    #Recorrer cada enlace y crear un nuevo valor en el diccionario
    for link in links:
        ctx[link.key] = link.url #El corchete lo abro para indicar que voy a crear una clave, se ha creado ya el diccionario con las redes sociales, con sus claves y valores que son redes sociales
    return ctx

