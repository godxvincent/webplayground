from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Documentación unit test https://docs.djangoproject.com/en/2.0/topics/testing/overview/
# Documentación hector https://github.com/hcosta/curso-python-udemy/blob/master/Fase%204%20-%20Temas%20avanzados/Tema%2016%20-%20Documentaci%C3%B3n%20y%20Pruebas/Lecci%C3%B3n%2004%20(Apuntes)%20-%20Unittest.ipynb
# Create your tests here.


class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('unittestuser', 'unittestuser@test.com', 'Callefalsa123')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='unittestuser').exists()
        self.assertEquals(exists, True)
