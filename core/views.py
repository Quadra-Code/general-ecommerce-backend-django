from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core import services

# Create your views here.

@api_view(['GET', 'POST'])
def get_all_brands(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_brands()
    elif request.method == 'POST':
        result = services.create_brand(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_brand(request):
    result = services.create_brand(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_brand(request):
    result = services.update_brand(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_brand(request, brand_id):
    result = services.delete_brand(brand_id=brand_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)