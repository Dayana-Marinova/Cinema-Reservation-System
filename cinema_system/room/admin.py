from django.contrib import admin
from room.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'number',
        'capacity',
    ]

admin.site.register(Room, RoomAdmin)
