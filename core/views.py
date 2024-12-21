from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core import services

# Create your views here.

@api_view(['GET'])
def home(request):
    ttee = services.get_all_brands()
    print(ttee)
    return Response(ttee.data)