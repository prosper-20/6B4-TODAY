from rest_framework import serializers
# from .models import User

from django.contrib.auth import get_user_model

User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)


    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    
    def save(self):
        user = User(
            email = self.validated_data.get("email"),
            username = self.validated_data.get("username")
        )
        password = self.validated_data.get("password")
        password2 = self.validated_data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"Response": "Both passwords must match"})
        
        user.set_password(password)
        user.save()
        return user