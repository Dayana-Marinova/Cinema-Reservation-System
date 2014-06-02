from django.contrib import admin
from film.models import Film


class FilmAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'priceOfTheThicket',
        'category',
        'typeOfFilm',
    ]
    search_fields = ['title']

admin.site.register(Film, FilmAdmin)
