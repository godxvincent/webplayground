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

# https://docs.djangoproject.com/en/2.0/topics/db/managers/


class ThreadManager(models.Manager):
    def find(self, user1, user2):
        # El objeto self es una referencia del query set Thread.objects.all()
        querySet = self.filter(users=user1).filter(users=user2)
        if (len(querySet) > 0):
            return querySet[0]
        return None

    def find_or_create(self, user1, user2):
        thread = self.find(user1, user2)
        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)
    updated = models.DateTimeField(auto_now=True)

    objects = ThreadManager()

    class Meta:
        ordering = ['-updated']


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
    instance.save()


m2m_changed.connect(messages_changed, sender=Thread.messages.through)
