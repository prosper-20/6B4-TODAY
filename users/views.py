from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView

class UserCreateView(APIView):
    def post(self, request, format=None):
        user_data = UserRegistrationSerializer(data=request.data)
        user_data.is_valid(raise_exception=True)
        user_data.save()
        message = {"Success": f"Hello {user_data.data.get('email')}, Your account has been created!!"}
        return Response(message, status=status.HTTP_201_CREATED)

