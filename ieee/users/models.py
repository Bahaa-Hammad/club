from django.db import models
from django.contrib.auth.models import User


class Account(User):
    users = models.Manager()

    class Meta:
        proxy = True
        ordering = ('username',)

    def get_user(username: str):
        user = Account.objects.get(username=username)

        if user:
            return user

        return None
