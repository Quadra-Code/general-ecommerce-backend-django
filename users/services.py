from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser, UserPhoneNumbers
from core.base_models import ResultView
from users.serializers import RegisterSerializer
from django.contrib.auth import authenticate
from users.utils import generate_jwt_token
import logging
# Create your services here.


def register_user_service(registration_data):
    result = ResultView()
    try:
        full_name = registration_data.get("full_name")
        phone_number = registration_data.get("phone_number")
        password = registration_data.get("password")
        confirm_password = registration_data.get("confirm_password")
        if not password or password != confirm_password:
            result.msg = f"{'Passwords Don\'t match' if password else 'Password is required'}"
        elif UserPhoneNumbers.objects.filter(phone_number=phone_number).exists() or CustomUser.objects.filter(username=phone_number).exists():
            result.msg = 'A user with this phone number already exists, please login'
        else:
            serialized_new_user_data = RegisterSerializer(data=registration_data)
            if serialized_new_user_data.is_valid():
                new_user = CustomUser.objects.create_user(
                    username=phone_number,
                    password=password,
                    first_name=full_name
                )
                UserPhoneNumbers.objects.create(
                    phone_number=phone_number,
                    is_main_number=True,
                    user=new_user,
                    created_by=new_user
                )
                result.data = new_user.to_dict()
                result.msg = f"User {new_user.first_name} created successfully"
                result.is_success = True
            else:
                result.msg = f'Error happened while serializing new user data'
                result.data = {'errors': serialized_new_user_data.errors, 'error messages': serialized_new_user_data.error_messages}
    except Exception as e:
        result.msg = f'Unexpected error happened while registering new user'
        result.data = {'error': str(e)}
    finally:
        return result


def login_user_service(login_data):
    result = ResultView()
    logger = logging.getLogger(__name__)
    try:
        username = login_data.get('username', '').strip() # what the empty quotes do ?
        password = login_data.get('password', '').strip()
        if not username or not password:
            result.msg = 'Username is required' if password else 'Password is required' if username  else 'Username & Password are required'
        else:
            user_to_auth = authenticate(username=username, password=password) # here django doesn't just check for the password but also check for the is_active field in the db, so no need to check on is_active
            if user_to_auth is None:
                logger.warning(f"Failed login attempt for username {username}.")
                result.msg = 'Invalid Credentials'
            elif not user_to_auth.is_active:
                result.msg = 'Account is not active. Please contact support'
            else:
                logger.info(f"User {user_to_auth.username} logged in successfully.")
                token = generate_jwt_token(user_to_auth)
                result.msg = 'Login Successful'
                result.data = {
                    'token': token,
                    'user': {
                        'id': user_to_auth.id,
                        'username': user_to_auth.username,
                        'full_name': user_to_auth.first_name
                    }
                }
                result.is_success = True
    except Exception as e:
        result.msg = f'Unexpected error happened while logging in user {username}.'
        result.data = {'error': str(e)}
    finally:
        return result


# def login_admin_service(username, password):
#     result = ResultView()
#     try:
#         print('in try')
#         if username and password:
#             print('there is username and password')
#             user = CustomUser.objects.get(username=username)
#             print('user found and it\'s', user, sep='=>')
#             if user.check_password(password):
#                 print('password is correct')
#                 result.data = user
#                 result.msg = f'User {user.username} logged in successfully'
#                 result.is_success = True
#             else:
#                 print('password is not correct')
#                 result.msg = 'Invalid Credentials'
#         else:
#             print('either username or password is missing')
#             result.msg = 'Username & Password are required' if not (username or password) else 'Username is required' if password else 'Password is required'
#     except Exception as e:
#         result.msg = f'Unexpected error happened while logging user {username} in.'
#         result.data = {'error': str(e)}
#     finally:
#         return result