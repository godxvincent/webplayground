from django.db import models
from django.contrib.auth.models import User
# https://docs.djangoproject.com/en/2.0/ref/signals/#m2m-changed
from django.db.models.signals import m2m_changed

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


def messages_changed(sender, **kwargs):
    # Recupera la instanaci del objeto que esta siendo modificado.
    instance = kwargs.pop("instance", None)
    # Recupera el tipo de acción que se esta haciendo sobre el objeto post_add o pre_add
    action = kwargs.pop("action", None)
    # Llaves de los objetos que estan siendo cargados
    pk_set = kwargs.pop("pk_set", None)
    print(instance, action, pk_set)

    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if (msg.user not in instance.users.all()):
                print("ups! not register user {}".format(msg.user))
                false_pk_set.add(msg_pk)

    pk_set.difference_update(false_pk_set)


m2m_changed.connect(messages_changed, sender=Thread.messages.through)
