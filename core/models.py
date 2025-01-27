from django.db import models
from core.base_models import BaseEntity
# Create your models here.

class Countries(BaseEntity):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f'Country Name => {self.name}'

class Cities(BaseEntity):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(
        to=Countries,
        on_delete=models.PROTECT,
        related_name="cities"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'country'], name='country_city_unique_constraint', violation_error_message='A Country must have unique city names')
        ]
        ordering = ['name']

    def __str__(self):
        return f'Country => {self.country.name} | City => {self.name}'

class Brands(BaseEntity):
    name_ar = models.CharField(max_length=100, unique=True)
    name_en = models.CharField(max_length=100, unique=True)
    logo_url = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return f'Brand Ar-Name: {self.name_ar}, Brand En-Name: {self.name_en}'

class Coupons(BaseEntity):
    code = models.CharField(max_length=7, unique=True)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Coupon Code: {self.code}, Discount: {self.discount}%, Coupon Is {"Active" if self.is_active else "Not Active"}'

class Sizes(BaseEntity):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Size Value Is: {self.name}'

class OrderStates(BaseEntity):
    name_ar = models.CharField(max_length=60, unique=True)
    name_en = models.CharField(max_length=60, unique=True)
    code = models.IntegerField(default=0, unique=True)
    color = models.CharField(max_length=7, unique=True)

    def __str__(self):
        return f'State Ar-Name: {self.name_ar}, State En-Name: {self.name_en}, State Code: {self.code}'

class Extras(BaseEntity):
    name_ar = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Extra Ar-Name: {self.name_ar},Extra En-Name: {self.name_en}, Extra Price: {self.price}'

class Categories(BaseEntity):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    parent = models.ForeignKey(to='self', on_delete=models.PROTECT, default=0)
    is_parent = models.BooleanField(default=False)
    level = models.IntegerField(default=0)
    image_url = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return f'Category Ar-Name: {self.name_ar}, Category En-Name: {self.name_en}, Category Level: {self.level}, Category Is {"Parent" if self.is_parent else "Not Parent"}, Parent Category Id Is {self.parent.id}'
