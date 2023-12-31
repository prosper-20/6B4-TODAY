from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class SongHomePage(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer



class SongDetailPage(GenericAPIView):
    serializer_class = SongSerializer
    def get(self, request, format=None, **kwargs):
        id = kwargs.get("id")
        slug = kwargs.get("slug")
        try:
            if id:
                current_song = Song.objects.get(id=id)
            elif slug:
                current_song = Song.objects.get(slug=slug)
            elif id and slug:
                current_song = Song.objects.get(id=id, slug=slug)
        except Song.DoesNotExist:
            return Response({"Error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serialized_song = SongSerializer(current_song)
        return Response(serialized_song.data, status=status.HTTP_200_OK)
    


class ArtistSongView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.filter(artist=self.request.user)
        return queryset


class MySongView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        print(self.request.user)
        queryset = Song.objects.filter(artist=self.request.user)
        return queryset
    


