from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .services import register_user
# Create your views here.


'''
{
    "username": "testuser",
    "password": "securepassword",
    "email": "test@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "image_url": "http://example.com/image.jpg",
    "country": "USA",
    "city": "New York",
    "address": "123 Main St",
    "postal_code": "10001"
}
{
    "phone_number": "testuser",
    "password": "securepassword",
    "confirm_password": "securepass",
    "full_name": "John han"
}
{
    "phone_number": "01555807172",
    "password": "securepassword",
    "confirm_password": "securepassword",
    "full_name": "John han"
}
'''
@api_view(['POST'])
def register(request):
    if request.data.get('password') and request.data.get('password') == request.data.get('confirm_password'):
        registeration_result = register_user(request.data)
        print(registeration_result)
        if registeration_result.is_success:
            return_status = status.HTTP_201_CREATED
        else:
            return_status = status.HTTP_500_INTERNAL_SERVER_ERROR if registeration_result.msg.__contains__('Unexpected') else status.HTTP_400_BAD_REQUEST
    else:
        return_status = status.HTTP_400_BAD_REQUEST
        msg = f"{'Password is required' if not request.data.get('password') else 'Passwords Don\'t match'}"
    return Response(registeration_result.to_dict(), status=return_status)