from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1',None,'test1234') #Crear unos usuarios y hilos para hacer pruebas
        self.user2 = User.objects.create_user('user2',None,'test1234')
        self.user3 = User.objects.create_user('user3',None,'test1234')

        #Creo un hilo manualmente
        self.thread = Thread.objects.create()

    #Se crean los tests
    def test__add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2) #Asigno los usuarios a la relación manytomany que espera usuarios - Añadir los usuarios al hilo
        self.assertEqual(len(self.thread.users.all()),2)

    def test_filter_thread_by_users(self): #Abajo en el método test_find_thread_with_custom_manage se hace más comodo
        self.thread.users.add(self.user1, self.user2) #Asigno los usuarios a la relación manytomany que espera usuarios
        #Recuperar el hilo de lo dos usuarios
        #threads = Thread.objects.filter(users=self.user1) #Todos los hilo donde forma parte el usuario 1
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2) #Todos los hilo donde forma parte el usuario 1 y usuario2
        self.assertEqual(self.thread, threads[0]) #Compruebo que el hilo de self.thread y la posicion 0 de la lista de hilos threads haiga concordancia

    #Comprobar un hilo cuando los usuarios no forman parte de el
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2) #Todos los hilo donde forma parte el usuario 1 y usuario2
        self.assertEqual(len(threads),0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2) #Asigno los usuarios a la relación manytomany que espera usuarios - Añadir los usuarios al hilo  
        message1 = Message.objects.create(user=self.user1, content="Buenas") #Mensaje lo cree usuario1 y le paso el contenido
        message2 = Message.objects.create(user=self.user2, content="Hola")
        self.thread.messages.add(message1,message2)
        self.assertEqual(len(self.thread.messages.all()),2) #Comparo la longitud de los mensajes que tengo en el hilo

        for message in self.thread.messages.all():
            print("({}) {}".format(message.user, message.content))

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Buenas") #Mensaje lo cree usuario1 y le paso el contenido
        message2 = Message.objects.create(user=self.user2, content="Hola")
        message3 = Message.objects.create(user=self.user3, content="Espia")
        self.thread.messages.add(message1,message2,message3)
        self.assertEqual(len(self.thread.messages.all()),2)


    def test_find_thread_with_custom_manage(self):
         self.thread.users.add(self.user1, self.user2)
         thread = Thread.objects.find(self.user1,self.user2)
         self.assertEqual(self.thread, thread) 

    def test_find_or_create_thread_with_custom_manage(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1,self.user2) #Para ver si se encuentra uno que ya existe
        self.assertEqual(self.thread, thread) 
        thread = Thread.objects.find_or_create(self.user1,self.user2) #Si no existe lo crea
        self.assertIsNotNone(thread)
