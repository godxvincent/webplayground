from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

# Esto es una forma de indicarle a django que se eecute algo en respuesta a unos cambios
# en un modelo como un trigger en django.

# Link documentación signals
# https://docs.djangoproject.com/en/2.0/topics/signals/


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    # El get verifica si en el kwargs hay algo con estado created si no retornamos False
    # por tanto solo se ejecuta si es creación
    if (kwargs.get('created', False)):
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear el perfil de un usuario.")
