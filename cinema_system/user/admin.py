from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'count_of_films',
        'count_of_comments',
    ]

admin.site.register(User, UserAdmin)
