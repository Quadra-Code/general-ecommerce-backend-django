from rest_framework_simplejwt.tokens import RefreshToken
from users.models import CustomUser, UserPhoneNumbers
from core.base_models import ResultView
from users.serializers import ChangePasswordSerializer, LoginSerializer, RegisterSerializer
from django.contrib.auth import authenticate, aauthenticate
from users.utils import extract_payload_from_jwt, generate_jwt_token
import logging
# Create your services here.


def register_user_service(registration_data):
    result = ResultView()
    try:
        full_name = registration_data.get("full_name", '')
        phone_number = registration_data.get("phone_number", '')
        password = registration_data.get("password", '')
        confirm_password = registration_data.get("confirm_password", '')
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
# async def login_user_service(login_data):
    result = ResultView()
    logger = logging.getLogger(__name__)
    try:
        username = login_data.get('username', '').strip() # what the empty quotes do ?
        password = login_data.get('password', '').strip()
        if not username or not password:
            result.msg = 'Username is required' if password else 'Password is required' if username  else 'Username & Password are required'
        else:
            serialized_login_data = LoginSerializer(data=login_data)
            if serialized_login_data.is_valid():
                user_to_auth = authenticate(username=username, password=password) # here django doesn't just check for the password but also check for the is_active field in the db, so no need to check on is_active
                # user_to_auth = await aauthenticate(username=username, password=password) # here django doesn't just check for the password but also check for the is_active field in the db, so no need to check on is_active
                if user_to_auth is None:
                    logger.warning(f"Failed login attempt for username {username}.")
                    result.msg = 'Invalid Credentials'
                elif not user_to_auth.is_active:
                    result.msg = 'Account is not active. Please contact support'
                else:
                    logger.info(f"User {user_to_auth.username} logged in successfully.")
                    # token = generate_jwt_token(user_to_auth)
                    # token_obj = generate_jwt_token(user_to_auth)
                    print(user_to_auth.groups.filter(name='client').first().permissions.all(), user_to_auth.user_permissions.all(), sep='\n=>')
                    print(user_to_auth.groups, user_to_auth.groups.all(), user_to_auth.get_group_permissions(), sep='\n=>')
                    result.msg = 'Login Successful'
                    result.data = {
                        # 'refresh_token': token_obj.get('refresh'),
                        # 'access_token': token_obj.get('access'),
                        # 'token': token,
                        'user': {
                            'id': user_to_auth.id,
                            'username': user_to_auth.username,
                            'full_name': user_to_auth.first_name
                        }
                    }
                    result.is_success = True
            else:
                result.msg = f'Error happened while serializing login data'
                result.data = {'errors': serialized_login_data.errors, 'error messages': serialized_login_data.error_messages}
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

def change_password_service(request):
    result = ResultView()
    try:
        token = request.headers.get('Authorization', '')
        old_password = request.data.get('old_password', '')
        new_password = request.data.get('new_password', '')
        confirm_new_password = request.data.get('confirm_new_password', '')
        if new_password != confirm_new_password:
            result.msg = 'Passwords Don\'t Match'
        elif not (token or old_password or new_password, confirm_new_password):
            result.msg = (
                'Old Password is required' if token and new_password and confirm_new_password
                else 'New Password is required' if token and confirm_new_password
                else 'Confirm New Password is required' if token
                else 'Unauthorized User' if new_password and confirm_new_password and old_password
                else 'Invalid Data'
            )
        else:
            serialized_change_password_data = ChangePasswordSerializer(data={
                'old_password': old_password,
                'new_password': new_password,
                'confirm_new_password': confirm_new_password
            })
            if serialized_change_password_data.is_valid():
                token_decode_result = extract_payload_from_jwt(token=str.replace(token, 'Bearer ', ''))
                if token_decode_result.get('error'):
                    result.data = {'error': token_decode_result.get('error')}
                    result.msg = token_decode_result.get('msg')
                else:
                    user_to_change_password = CustomUser.objects.filter(id=token.id).first()
                    if user_to_change_password:
                        user_to_change_password.set_password(new_password)
                        # user_to_change_password.save()
                        result.data = {'username': token.username}
                        result.msg = f'Changed password for user {token.username} successfully'
                        result.is_success = True
                    else:
                        result.msg = 'Unauthorized User'
            else:
                result.msg = 'Error happen while serializing new password data'
    except Exception as e:
        result.msg = f'Unexpected error happened while changing password{f" for user {token.username}" if token.username else ""}'
        result.data = {'error': str(e)}
    finally:
        return result