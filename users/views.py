from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .services import register_user
# Create your views here.

@api_view(['POST'])
def register(request):
    print(request.data)
    registeration_result = register_user(request.data.email, request.data.password)
    print(registeration_result)
    if registeration_result.is_success:
        return Response({'data': registeration_result.data, 'msg': registeration_result.msg}, status=status.HTTP_201_CREATED)
    else:
        return Response({'msg': registeration_result.msg, 'data': registeration_result.data}, status=status.HTTP_400_BAD_REQUEST)