from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import Countries, Cities
from core.base_models import BaseEntity
# Create your models here.

class CustomUser(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    image_url = models.CharField(max_length=1000, null=True, blank=True)

    def to_dict(self):
        main_phone_number = self.userphonenumbers_set.filter(is_main_number=True).first()
        main_address = self.useraddresses_set.filter(is_main_address=True).first()
        return {
            'id': self.id,
            'full_name': f"{self.first_name} {self.last_name}",
            'username': self.username,
            'main_phone_number': main_phone_number.phone_number.strip() if main_phone_number else None,
            'main_address': main_address.address.strip() if main_address else None,
            'email': self.email,
            'email_confirmed': self.email_confirmed,
            'date_joined': self.date_joined.strftime('%a %d %b %Y, %H:%M:%S %p') if self.date_joined else None,
            'last_login': self.last_login.strftime('%a %d %b %Y, %H:%M:%S %p') if self.last_login else None,
            'is_superuser': self.is_superuser,
            'is_staff': self.is_staff,
            'is_active': self.is_active,
            'image_url': self.image_url
        }
    def __str__(self):
        main_phone_number = self.userphonenumbers_set.filter(is_main_number=True).first()
        main_address = self.useraddresses_set.filter(is_main_address=True).first()
        full_name = f"{self.first_name} {self.last_name}".strip()
        phone_str = f"| Main Phone Number: {main_phone_number.phone_number}" if main_phone_number else ""
        address_str = f"| Main Address: {main_address.address.strip()} {main_address.city.strip()} {main_address.country.strip()}" if main_address else ""
        return f"User Data => ID: {self.id} | Full Name: {full_name} | Is Active: {self.is_active} {phone_str} {address_str}".strip()

class UserPhoneNumbers(BaseEntity):
    phone_number = models.CharField(max_length=20, unique=True)
    phone_number_confirmed = models.BooleanField(default=False)
    is_main_number = models.BooleanField(default=False)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Phone Number: {self.phone_number} | User Full Name: {self.user.first_name}"

class UserAddresses(BaseEntity):
    country = models.ForeignKey(to=Countries, on_delete=models.PROTECT)
    city = models.ForeignKey(to=Cities, on_delete=models.PROTECT)
    address = models.CharField(max_length=600)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    is_main_address = models.BooleanField(default=False)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    class Meta:
        # unique_together = ('user', 'country', 'city', 'address') old way
        constraints = [
            models.UniqueConstraint(fields=['user', 'country', 'city', 'address'], name='Unique_country_city_address_per_user', violation_error_message='Country, City and Address must be unique for each user')
        ]

    def __str__(self):
        return f"User Full Name => {self.user.first_name} | Country => {self.country} | City => {self.city} | Address => {self.address}{f' | Postal Code => {self.postal_code}' if self.postal_code else ''}"
