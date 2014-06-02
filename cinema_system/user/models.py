from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    count_of_films = models.PositiveIntegerField(default=0)
    count_of_comments = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.count_of_films
