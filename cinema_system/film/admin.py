from django.contrib import admin
from film.models import Film, Reservation


class FilmAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'price_of_the_thicket',
        'category',
        'type_of_film',
    ]
    search_fields = ['title']

admin.site.register(Film, FilmAdmin)


class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'film',
    ]

admin.site.register(Reservation, ReservationAdmin)
