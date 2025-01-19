import jwt
from rest_framework_simplejwt.tokens import RefreshToken
# from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# not valid with simplejwt authentication
# def generate_jwt_token(user):
#     payload = {
#         'id': user.id,
#         'username': user.username,
#         # 'full_name': user.first_name,
#         'exp': datetime.now() + timedelta(days=3),
#         # 'iat': datetime.now(),
#         'iss': 'general_ecommerce_backend'
#     }
#     token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
#     return token


def extract_payload_from_jwt(token):
    try:
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        print(f'payload is => {payload}')
        return payload
    except jwt.ExpiredSignatureError as e:
        return {'error': str(e), 'msg': 'Token is expired'}
    except jwt.InvalidTokenError as e:
        print('invalid token error', e, sep='\n=>')
        return {'error': str(e), 'msg': 'Invalid token'}
    except Exception as e:
        return {'error': str(e), 'msg': 'Unexpected error happened while decoding token'}
