from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage #Sirve para crear la estructura de un mensaje y uncluye un método para enviarlo
from .forms import ContactForm

# Create your views here.

def contact(request):
    #print("Tipo de petición : {}".format(request.method)) #Para ver el tipo de petición que se ha hecho
    contact_form = ContactForm()#Creo la plantilla vacía

    if request.method == "POST":#Verifico si se han enviado por post algun dato
        contact_form = ContactForm(data=request.POST) #Le paso un campo que es el diccionario que hay en el request post, incluye los campos que he enviado, relleno la plantilla con los datos automaticamente
        if contact_form.is_valid(): #Para ver si los datos estan rellenados correctamente
            name = request.POST.get('name','') #Como es un diccionario puedo usar el accesor get, le digo que me devuelva el valor que hay en la clave name y no me lo devuelva vacía
            email = request.POST.get('email','') 
            content = request.POST.get('content','') 
            #Pienso que ta todo bien perro y redirecciono
            #return redirect(reverse('contact')+"?ok")#Al reverse le paso el path contact, ya es como un template tag url y un mensaje en crudo   
                
            #Envío el corre y redirecciono
            email = EmailMessage(
               "La Caffettie: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,content),#cuerpo,
                "no-contestar@inbox.mailtrap.io",#email_origen, para hacer entender que si alguien contesta a este correo nadie le va responder, se pone el personal o empresa que concuerde con el dominio que este configurado
                ["positivemind6969@outlook.com"],#email_destino, lista de emails donde quiero enviar los mensajes
                reply_to=[email] #Donde paso, el email donde va responder la persona que recibira el correo, que la persona que se pone en contacto para que pueda responder en el mensaje y ya se le responda
            )

           #Enviar el email
            try:
                email.send()
                #Todo ha ido bien, redirecciono a ok
                return redirect(reverse('contact')+"?ok") 
            except:
                #Algo se jodio, redirecciono a fail
                return redirect(reverse('contact')+"?fail")         
           
        
    return render(request,"contact.html",{'form':contact_form})
