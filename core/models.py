from django.db import models
from users.models import CustomUser
# Create your models here.

class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name="%(class)s_created", on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(CustomUser, related_name="%(class)s_updated", on_delete=models.SET_NULL, null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    class Meta:
        abstract = True

class Brands(BaseEntity):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    logo_url = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return f'Brand Ar-Name: {self.name_ar}, Brand En-Name: {self.name_en}'

class Coupons(BaseEntity):
    code = models.CharField(max_length=7)
    discount = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'Coupon Code: {self.code}, Discount: {self.discount}%, Coupon Is {"Active" if self.is_active else "Not Active"}'

class Sizes(BaseEntity):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Size Value Is: {self.name}'

class OrderStates(BaseEntity):
    name_ar = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    code = models.IntegerField(default=0)

    def __str__(self):
        return f'State Ar-Name: {self.name_ar}, State En-Name: {self.name_en}, State Code: {self.code}'

class Extras(BaseEntity):
    name_ar = models.CharField(max_length=60)
    name_en = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Extra Ar-Name: {self.name_ar},Extra En-Name: {self.name_en}, Extra Price: {self.price}'

class Categories(BaseEntity):
    name_ar = models.CharField(max_length=100, default='')
    name_en = models.CharField(max_length=100, default='')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, default=0)
    is_parent = models.BooleanField(default=False)
    level = models.IntegerField(default=0)
    image_url = models.CharField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return f'Category Ar-Name: {self.name_ar}, Category En-Name: {self.name_en}, Category Level: {self.level}, Category Is {"Parent" if self.is_parent else "Not Parent"}, Parent Category Id Is {self.parent.id}'
