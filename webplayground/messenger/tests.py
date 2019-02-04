# Desarrollo orientado por pruebas.
# https://medium.freecodecamp.org/learning-to-test-with-python-997ace2d8abe
# https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas
# https://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137
# https://dzone.com/articles/tdd-python-5-minutes


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Thread


# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')
        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_user(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_user(self):
        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(len(threads), 0)

    def test_add_messages_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola mundo")
        message2 = Message.objects.create(user=self.user2, content="Hola, que tal!")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))

    def test_add_messages_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Hola mundo")
        message2 = Message.objects.create(user=self.user2, content="Hola, que tal!")
        message3 = Message.objects.create(user=self.user3, content="Soy un espia")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)
