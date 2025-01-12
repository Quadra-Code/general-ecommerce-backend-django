from rest_framework import serializers
from .models import CustomUser

# Create your serializers here.

class RegisterSerializer(serializers.Serializer): # here i didn't use model serializer because i only need some fileds for the registration process
    full_name = serializers.CharField(max_length=40, required=True, min_length=6)
    phone_number = serializers.CharField(max_length=20, required=True, min_length=8)
    password = serializers.CharField(write_only=True)
    # username = serializers.CharField(max_length=150)
    # email = serializers.EmailField(required=True)
    # first_name = serializers.CharField(max_length=25, required=False, allow_blank=True)
    # last_name = serializers.CharField(max_length=25, required=False, allow_blank=True)
    # image_url = serializers.CharField(max_length=1000, required=False, allow_blank=True)

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)