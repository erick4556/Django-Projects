from django.test import TestCase
from .models import Profile #El modelo que voy a usar para el test
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self): #Método que voy a sobreescribir. Preparo la prueba aquí
        User.objects.create_user('test','test@hotmail.com','test1234') #Crear un usuario de prueba. El create_user es un modelo propio de user donde me deja meterle una contraseña y solito la cifra

    def test_profile_exists(self): #Método que voy a sobreescribir, siempre tiene que iniciar con la palabra test_ y después cualquier nombre que quiera
        exists = Profile.objects.filter(user__username='test').exists() #Para ver si en Profile hay un user igual a test y con el exists me devuelve un True o False
        self.assertEqual(exists, True) #Compruebo que el exists tenga el valor True de huevo a huevo