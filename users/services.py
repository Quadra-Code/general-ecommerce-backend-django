from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, UserPhoneNumbers
from core.base_models import ResultView
from users.serializers import RegisterSerializer
# Create your services here.

def register_user(registeration_data):
    result = ResultView()
    try:
        full_name = registeration_data.get("full_name")
        first_name=f'{full_name.split(' ')[0] if full_name.__contains__(' ') else full_name}'
        last_name = ' '.join(full_name.split(' ')[1:])
        phone_number = registeration_data.get("phone_number")
        password = registeration_data.get("password")
        if UserPhoneNumbers.objects.filter(phone_number=phone_number).exists() or CustomUser.objects.filter(username=phone_number).exists():
            result.msg = 'A user with this phone number already exists, please login'
        else:
            serialized_new_user_data = RegisterSerializer(data=registeration_data)
            if serialized_new_user_data.is_valid():
                # new_user = CustomUser.objects.create_user(username=phone_number, password=password, first_name=first_name, last_name=last_name)
                test: CustomUser = {'id': 1, 'username': phone_number, 'password': password, 'first_name':first_name, 'last_name':last_name}
                tt = UserPhoneNumbers.objects.create(phone_number=phone_number, is_main_number=True, user = test)#.save()
                print(tt)
                # print(new_user, new_user.id)
                # CustomUser.objects.create_user(username=email.split('@')[0], password=password, email=email, **extra_fields)
                result.is_success = True
                # result.data = new_user
                # user_display_name = f"{new_user.first_name} {new_user.last_name}" if new_user.first_name else new_user.usernamr
                # result.msg = f"User {user_display_name} created successfully"
            else:
                result.msg = f'Error happened while serializing new user data.\nError Message: {serialized_new_user_data.errors}'
                result.data = {'errors': serialized_new_user_data.errors, 'error messages': serialized_new_user_data.error_messages}
    except Exception as e:
        result.msg = f'Unexpected Error happened while registering new user. | Error Message: {e}'
        result.data = {'error': str(e)}
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
    