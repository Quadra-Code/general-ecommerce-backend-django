from rest_framework import serializers
from core import models

# Create your serializers here.
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brands
        fields = ['id', 'name_ar', 'name_en', 'logo_url']
