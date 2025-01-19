from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.services import register_user_service, login_user_service, change_password_service#, login_admin_service
# Create your views here.


'''
input
{
    "phone_number": "01555807172",
    "password": "securepassword",
    "confirm_password": "securepassword",
    "full_name": "John han"
}
output
{
    "is_success": true,
    "data": "User Data => ID: 1 | Full Name: John han | Main Phone: 01555807172"
    },
    "msg": "User John han created successfully"
}
'''

@api_view(['POST'])
def register(request):
    registration_result = register_user_service(request.data)
    status_code = (
        status.HTTP_201_CREATED if registration_result.is_success
        else status.HTTP_400_BAD_REQUEST
    )
    return Response(registration_result.to_dict(), status=status_code)

'''
input
{
    "username": "01555807172",
    "password": "securepassword"
}
output
{
    "is_success": true,
    "data": {
        "token": "generated token",
        "user": {
            "id": 1,
            "username": "01555807172",
            "full_name": "John han"
        }
    },
    "msg": "Login Successful"
}
'''
@api_view(['POST'])
def login_user(request):
    # print(request.body, request.data, request.headers, sep='\n=>')
    login_result = login_user_service(request.data)
    # login_result = await login_user_service(request.data)
    status_code = (
        status.HTTP_202_ACCEPTED if login_result.is_success
        else status.HTTP_400_BAD_REQUEST
    )
    return Response(login_result.to_dict(), status=status_code)

# @api_view(['POST'])
# def login_admin(request):
#     login_result = login_admin_service(request.data.get('username'), request.data.get('password'))
#     status_code = (
#         status.HTTP_202_ACCEPTED if login_result.is_success
#         else status.HTTP_403_FORBIDDEN if login_result.msg.__contains__('not active')
#         else status.HTTP_400_BAD_REQUEST
#     )
#     return Response(login_result.to_dict(), status=status_code)

'''
input
{
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiIwMTU1NTgwNzE3MiIsImZ1bGxfbmFtZSI6IkpvaG4gaGFuIiwiZXhwIjoxNzM2OTM4OTM0LCJpYXQiOjE3MzY5Mzg3NTQsImlzcyI6ImdlbmVyYWxfZWNvbW1lcmNlX2JhY2tlbmQifQ.g4VSe9FfDMrfDycMX2y5YZMNTUuzNIT_IErP-OYlR2E",
    "old_password": "securepassword",
    "new_password": "123",
    "confirm_new_password": "123"
}
'''

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def change_password(request):
    print('got here in the view')
    change_password_result = change_password_service(request)
    status_code = (
        status.HTTP_202_ACCEPTED if change_password_result.is_success
        else status.HTTP_400_BAD_REQUEST
    )
    return Response(change_password_result.to_dict(), status=status_code)

'''
pip install twilio => all 15 following packages
aiohappyeyeballs-2.4.4     ||     aiohttp-3.11.11
aiohttp-retry-2.8.3        ||     aiosignal-1.3.2
attrs-24.3.0               ||     certifi-2024.12.14
charset-normalizer-3.4.1   ||     frozenlist-1.5.0
propcache-0.2.1            ||     requests-2.32.3
twilio-9.4.3               ||     urllib3-2.3.0
idna-3.10     ||    multidict-6.1.0    ||   yarl-1.18.3
'''
# from twilio.rest import Client
# @api_view(['GET'])
# def test_sms(request):
#     account_sid = 'get from .env'
#     auth_token = 'get from .env'
#     client = Client(account_sid, auth_token)
#     verification = client.verify.v2.services('VA853ed765c0c235b050c6332aae0f1e41').verifications.create(to='+201118069749', channel='sms')
#     print(verification.status, verification.valid, verification.sna, verification.to, verification.sid, sep='\n=>')
'''
{
  "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "to": "+201118069749",
  "channel": "sms",
  "status": "pending",
  "valid": false,
  "date_created": "2015-07-30T20:00:00Z",
  "date_updated": "2015-07-30T20:00:00Z",
  "lookup": {},
  "amount": null,
  "payee": null,
  "send_code_attempts": [
    {
      "time": "2015-07-30T20:00:00Z",
      "channel": "SMS",
      "attempt_sid": "VLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "sna": null,
  "url": "http s://verify.twilio.com/v2/Services/VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Verifications/VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
}
'''
# def check_test_sms_otp(request):#check the otp
#     account_sid = 'get from .env'
#     auth_token = 'get from .env'
#     client = Client(account_sid, auth_token)
#     verification_check = client.verify.v2.services('VA853ed765c0c235b050c6332aae0f1e41').verification_checks.create(to='+201118069749', code=request.data.get('code'))
#     print(verification_check.status, verification_check.valid, verification_check.to, verification_check.sid, sep='\n=>')
'''
output should be
{
  "sid": "VEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "service_sid": "VAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "to": "+201118069749",
  "channel": "sms",
  "status": "approved",
  "valid": true,
  "amount": null,
  "payee": null,
  "sna_attempts_error_codes": [],
  "date_created": "2015-07-30T20:00:00Z",
  "date_updated": "2015-07-30T20:00:00Z"
}
'''