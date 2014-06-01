from django.db import models


class Film(models.Model):
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False, max_length=300)
    rating = rating = models.PositiveIntegerField(default=0)
    priceOfTheThicket = models.PositiveIntegerField(default=0)
    language = models.CharField(blank=False, max_length=20)
    time = models.PositiveIntegerField(default=0)
    category = models.CharField(blank=False, max_length=20)
    subtitles = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)
    typeOfFilm = models.CharField(blank=False, max_length=10)

    def __unicode__(self):
        return self.title
