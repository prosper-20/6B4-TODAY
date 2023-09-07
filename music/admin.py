from django.contrib import admin
from .models import Album, Genre, Song


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class SongAdmin(admin.ModelAdmin):
    list_display = ["artist", "name", "release_date"]
    list_filter = ["artist"]
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ["name"]


admin.site.register(Song, SongAdmin)
