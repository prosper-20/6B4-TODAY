from django.contrib import admin
from .models import Profile
from django.conf import settings

from django.contrib.auth import get_user_model

User = get_user_model()


admin.site.register(User)

admin.site.register(Profile)
