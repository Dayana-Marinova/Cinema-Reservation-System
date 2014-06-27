from django.db import models
from user.models import User
from seat.models import Seat

class Film(models.Model):
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False, max_length=300)
    rating = models.PositiveIntegerField(default=0)
    price_of_the_thicket = models.PositiveIntegerField(default=0)
    language = models.CharField(blank=False, max_length=20)
    time = models.PositiveIntegerField(default=0)
    category = models.CharField(blank=False, max_length=20)
    subtitles = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)
    type_of_film = models.CharField(blank=False, max_length=10)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    user = models.ForeignKey(User)
    film = models.ForeignKey(Film)
