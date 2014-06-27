from django.db import models


class Room(models.Model):
    number = models.PositiveIntegerField(default=0)
    capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.number)
