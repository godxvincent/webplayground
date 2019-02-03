from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

# Link custom_upload_to https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.FileField.upload_to


def custom_upload_to(instance, filename):
    old_instanace = Profile.objects.get(pk=instance.pk)
    old_instanace.avatar.delete()
    return 'profile/' + filename


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Se ha cambiado el directorio por una función
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    # Esto fue agregado porque en la consola sale un warning indicando que los resultados de la paginaciónote
    # podria ser inesperado debido a que no esta ordenada la querysetself.
    # Pagination may yield inconsistent results with an un
    # ordered object_list: <class 'registration.models.Profile'> QuerySet.
    class Meta:
        ordering = ['user__username']
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
