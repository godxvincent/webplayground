from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)

# Desarrollo orientado por pruebas.
# https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe
# https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas
# https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137
# https://dzone.com/articles/tdd-python-5-minutes
