from django.contrib import admin
from .models import Album, Genre, Song

admin.site.register([Album, Genre])


class SongAdmin(admin.ModelAdmin):
    list_display = ["artist", "name", "release_date"]
    list_filter = ["artist"]
    list_editable = ["name"]


admin.site.register(Song, SongAdmin)
