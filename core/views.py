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
    
@api_view(['GET', 'POST'])
def get_all_coupons(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_coupons()
    elif request.method == 'POST':
        result = services.create_coupon(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_coupon(request):
    result = services.create_coupon(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_coupon(request):
    result = services.update_coupon(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_coupon(request, coupon_id):
    result = services.delete_coupon(coupon_id=coupon_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_sizes(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_sizes()
    elif request.method == 'POST':
        result = services.create_size(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_size(request):
    result = services.create_size(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_size(request):
    result = services.update_size(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_size(request, size_id):
    result = services.delete_size(size_id=size_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_orderStates(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_orderStates()
    elif request.method == 'POST':
        result = services.create_orderState(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_orderState(request):
    result = services.create_orderState(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_orderState(request):
    result = services.update_orderState(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_orderState(request, orderState_id):
    result = services.delete_orderState(orderState_id=orderState_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_extras(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_extras()
    elif request.method == 'POST':
        result = services.create_extra(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_extra(request):
    result = services.create_extra(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_extra(request):
    result = services.update_extra(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_extra(request, extra_id):
    result = services.delete_extra(extra_id=extra_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_categories(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_categories()
    elif request.method == 'POST':
        result = services.create_category(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_category(request):
    result = services.create_category(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_category(request):
    result = services.update_category(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request, category_id):
    result = services.delete_category(category_id=category_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_cities(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_cities()
    elif request.method == 'POST':
        result = services.create_city(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_city(request):
    result = services.create_city(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_city(request):
    result = services.update_city(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_city(request, city_id):
    result = services.delete_city(city_id=city_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def get_all_countries(request):
    print(request)
    result = None
    if request.method == 'GET':
        result = services.get_all_countries()
    elif request.method == 'POST':
        result = services.create_country(request_data=request.data)
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response(result.data, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_all_countries_cities(request):
    result = services.get_all_countries_cities()
    if result.is_success:
        return Response(result.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": result.msg}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_country(request):
    result = services.create_country(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_country(request):
    result = services.update_country(request_data=request.data)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_country(request, country_id):
    result = services.delete_country(country_id=country_id)
    if result.is_success:
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    
