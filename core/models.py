from django.db import models

# Create your models here.
class Base_Entity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # created_by = models.IntegerField()
    updated = models.DateTimeField()
    # updated_by = models.IntegerField()
    deleted = models.DateTimeField()
    # deleted_by = models.IntegerField()
    is_deleted = models.BooleanField(default=False, null=False)

class Categories(models.Model, Base_Entity):
    name_ar = models.CharField(null=False, max_length=100, default='')
    name_en = models.CharField(null=False, max_length=100, default='')
    parent_category_id = models.IntegerField(null=False, default=0)
    is_parent = models.BooleanField(null=False, default=False)
    level = models.IntegerField(null=False, default=0)
    image = models.CharField(blank=True, null=True)