from django.urls import path
from .views import UserCreateView
from rest_framework.authtoken import views



urlpatterns = [
    path('signin/', views.obtain_auth_token, name="signin"),
    path("signup/", UserCreateView.as_view(), name="signup")
]