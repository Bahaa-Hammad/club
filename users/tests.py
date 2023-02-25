from django.test import TestCase
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model


class UsersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username="normaluser", password="DevOps")
        self.assertEqual(user.username, "normaluser")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNotNone(user.email)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username="superuser", password="DevOps")
        self.assertEqual(admin_user.username, "superuser")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNotNone(admin_user.email)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username="superuser", password="DevOps", is_superuser=False)

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testUser', password='DevOps')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='testUser', password='DevOps')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='DevOps')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='testUser', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
