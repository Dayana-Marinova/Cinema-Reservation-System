from django.db import models
from room.models import Room


class Seat(models.Model):
    room = models.ForeignKey(Room)
    number = models.PositiveIntegerField(default=0)
    taken = models.BooleanField(default=False)

    def __unicode__(self):
        return self.number
