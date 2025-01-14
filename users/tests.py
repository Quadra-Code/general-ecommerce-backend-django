from django.test import TestCase
from rest_framework.test import APIClient
from users.services import register_user
# Create your tests here.

class RegisterUserServiceTest(TestCase):
    def test_register_user_success(self):
        data = {
            "full_name": "John Doe",
            "phone_number": "1234567890",
            "password": "securePassword",
            "confirm_password": "securePassword",
        }
        result = register_user(data)
        self.assertTrue(result.is_success)
        self.assertEqual(result.msg, "User John Doe created successfully")

    def test_register_user_password_mismatch(self):
        data = {
            "full_name": "John Doe",
            "phone_number": "1234567890",
            "password": "securePassword",
            "confirm_password": "differentPassword",
        }
        result = register_user(data)
        self.assertFalse(result.is_success)
        self.assertEqual(result.msg, "Passwords don't match")

class RegisterUserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user_view_success(self):
        data = {
            "full_name": "John Doe",
            "phone_number": "1234567890",
            "password": "securePassword",
            "confirm_password": "securePassword",
        }
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("created successfully", response.data["msg"])

    def test_register_user_view_password_mismatch(self):
        data = {
            "full_name": "John Doe",
            "phone_number": "1234567890",
            "password": "securePassword",
            "confirm_password": "differentPassword",
        }
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["msg"], "Passwords don't match")