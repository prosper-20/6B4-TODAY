from django.db import models
import uuid

from django.conf import settings

User = settings.AUTH_USER_MODEL

class Genre(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()


    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    release_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='album_covers/')
   
    def __str__(self):
        return self.title
   

class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    cover_image = models.ImageField(upload_to="song_covers")
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    other_artist = models.CharField(max_length=300, blank=True, null=True)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
