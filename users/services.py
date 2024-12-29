from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from core.services import ResultView
from users.serializers import RegisterSerializer
# Create your services here.

def register_user(email, password, **extra_fields):
    result = ResultView()
    print(email, password, extra_fields)
    print(**extra_fields)
    try:
        if CustomUser.objects.filter(email=email).exists():
            result.msg = 'A user with this email already exists'
        else:
            print(**extra_fields)
            serialized_new_user_data = RegisterSerializer(data={'email': email, 'password': password, **extra_fields})
            if serialized_new_user_data.is_valid():
                new_user = CustomUser.objects.create_user(username=email.split('@')[0], password=password, email=email, **extra_fields)
                # new_user.save()
                result.is_success = True
                result.data = new_user
                user_display_name = f"{new_user.first_name} {new_user.last_name}" if new_user.first_name else new_user.email
                result.msg = f"User {user_display_name} created successfully"
            else:
                result.msg = f'Error happened while serializing new user data.\nError Message: {serialized_new_user_data.errors}'
                result.data = {'errors': serialized_new_user_data.errors, 'error messages': serialized_new_user_data.error_messages}
    except Exception as e:
        result.msg = f'Error happened while registering new user.\nError Message: {e}'
        result.data = {'error': e}
    finally:
        return result

def login_user(username, password):
    result = ResultView()
    try:
        if username and password:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                result.is_success = True
                result.data = user
                result.msg = f'User {user.username} logged in successfully'
            else:
                result.msg = 'Password is incorrect'
        else:
            result.msg = 'Username & Password are required' if not (username or password) else 'Username is required' if password else 'Password is required'
    except Exception as e:
        result.msg = f'Error happened while logging user {username} in.\n Error Message: {e}'
        result.data = {'error': e}
    finally:
        return result
    