from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    image_url = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=25, null=True, blank=True)
    city = models.CharField(max_length=25, null=True, blank=True)
    address = models.CharField(max_length=600, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)

    # Example of relationships:
    # product_reviews = models.ManyToManyField('ProductReview', blank=True, related_name='user_reviews')

    def __str__(self):
        return self.username  # This will display the username of the user