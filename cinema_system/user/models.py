from django.db import models
from django.contrib.auth.models import User


class User(User):
    USERNAME_FIELD = 'username'
    #user = models.ForeignKey(User, unique=True, related_name='profile')
    count_of_films = models.PositiveIntegerField(default=0)
    count_of_comments = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.count_of_films
