from django.urls import path
from .views import SongHomePage, SongDetailPage

#127.0.0.1:8000/songs/

urlpatterns = [
    path("all/", SongHomePage.as_view(), name="song"),
    path("<uuid:id>/", SongDetailPage.as_view(), name="song-detail"),
    path("<slug:slug>/", SongDetailPage.as_view(), name="song-detail2"),
    path("<uuid:id>/<slug:slug>/", SongDetailPage.as_view(), name="song-detail3")

]