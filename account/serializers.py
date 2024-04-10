from django.contrib.auth.forms import PasswordResetForm
from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age', 'country', 'residence')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        # Validate if the provided email address exists in the user database
        PasswordResetForm(data={'email': value}).is_valid()
        return value
