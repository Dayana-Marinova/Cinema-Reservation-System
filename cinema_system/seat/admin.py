from django.contrib import admin
from seat.models import Seat


class SeatAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'number',
        'room',
    ]

admin.site.register(Seat, SeatAdmin)
