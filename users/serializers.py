from rest_framework import serializers
from .models import CustomUser

# Create your serializers here.

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=25, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=25, required=False, allow_blank=True)
    image_url = serializers.CharField(max_length=1000, required=False, allow_blank=True)
    country = serializers.CharField(max_length=25, required=False, allow_blank=True)
    city = serializers.CharField(max_length=25, required=False, allow_blank=True)
    address = serializers.CharField(max_length=600, required=False, allow_blank=True)
    postal_code = serializers.CharField(max_length=10, required=False, allow_blank=True)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)