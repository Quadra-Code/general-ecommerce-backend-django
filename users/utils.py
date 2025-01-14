import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt_token(user):
    payload = {
        'id': user.id,
        'username': user.username,
        'full_name': user.first_name,
        'exp': datetime.now() + timedelta(minutes=3),
        'iat': datetime.now(),
        'iss': 'general_ecommerce_backend'
    }
    token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm='HS256')
    return token