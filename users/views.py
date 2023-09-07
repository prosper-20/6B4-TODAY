from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

class UserCreateView(APIView):
    serializer_class =  UserRegistrationSerializer
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        user_data = UserRegistrationSerializer(data=request.data)
        user_data.is_valid(raise_exception=True)
        user_data.save()
        message = {"Success": f"Hello {user_data.data.get('email')}, Your account has been created!!"}
        return Response(message, status=status.HTTP_201_CREATED)

