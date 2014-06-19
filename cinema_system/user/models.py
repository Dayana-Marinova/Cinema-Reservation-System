from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    count_of_films = models.PositiveIntegerField(default=0)
    count_of_comments = models.PositiveIntegerField(default=0)

