from rest_framework import serializers
from core import models

# Create your serializers here.
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brands
        fields = ['id', 'name_ar', 'name_en', 'logo_url']

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Coupons
        fields = ['id', 'code', 'discount', 'is_active']

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sizes
        fields = ['id', 'name']

class OrderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderStates
        fields = ['id', 'name_ar', 'name_en','code','color']

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Extras
        fields = ['id', 'name_ar', 'name_en','price']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ['id', 'name_ar', 'name_en','parent','is_parent','level','image_url']

class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = models.Cities
        fields = ['id', 'name', 'country', 'country_name'] 

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Countries
        fields = ['id', 'name'] 

class CountryWithCitiesSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True) 

    class Meta:
        model = models.Countries
        fields = ['id', 'name', 'cities']

