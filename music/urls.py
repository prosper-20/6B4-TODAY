from django.urls import path
from .views import SongHomePage, SongDetailPage, MySongView

#127.0.0.1:8000/songs/

urlpatterns = [
    path("all/", SongHomePage.as_view(), name="song"),
    path("my-songs/", MySongView.as_view(), name="my-songs"),
    path("<uuid:id>/", SongDetailPage.as_view(), name="song-detail"),
    path("<slug:slug>/", SongDetailPage.as_view(), name="song-detail2"),
    path("<uuid:id>/<slug:slug>/", SongDetailPage.as_view(), name="song-detail3")

]