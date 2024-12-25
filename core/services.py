from django.core.exceptions import ObjectDoesNotExist
from core import models
from core import serializers
# Create your services here.

class ResultView():
    def __init__(self, is_success=True, data=None, msg=''):
        self.is_success = is_success
        self.data = data
        self.msg = msg

    def __str__(self):
        return f'Operation Is{'' if self.is_success else 'n\'t'} Successful\nData: {self.data}\nMsg: {self.msg}'


#region Brand Region
def get_all_brands():
    result = ResultView()
    try:
        all_brands = models.Brands.objects.all()
        serialized_brands = serializers.BrandSerializer(all_brands, many=True)
        result.is_success = True
        result.data = serialized_brands.data
        result.msg = 'All Brands Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All Brands.\nError Message: {e}'
    finally:
        return result

def create_brand(request_data):
    result = ResultView()
    try:
        serialized_new_brand = serializers.BrandSerializer(data=request_data)
        if serialized_new_brand.is_valid():
            serialized_new_brand.save()
            result.is_success = True
            result.data = serialized_new_brand.data
            result.msg = 'New Brand Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New Brand.\nError Message: {serialized_new_brand.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New Brand.\nError Message: {e}'
    finally:
        return result

def update_brand(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_brand = models.Brands.objects.get(id=request_data.id)
            serialized_updated_brand = serializers.BrandSerializer(old_brand, data=request_data)
            if serialized_updated_brand.is_valid():
                serialized_updated_brand.save()
                result.is_success = True
                result.data = serialized_updated_brand.data
                result.msg = 'Brand Updated Successfully'
            else:
                result.msg = f'New Updated Brand Data Is Not Valid.\nError Message: {serialized_updated_brand.errors}'
        else:
            result.msg = f'There is no brand id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating Brand.\nError Message: {e}'
    finally:
        return result

def delete_brand(brand_id):
    result = ResultView()
    try:
        # here we can check if there is any related entities (products) if the business logic requires the brand field not to be null
        # else we can delete and the models on delete will set the field to null
        # if models.Products.objects.filter(brand_id=brand_id).exists():
        #     result.msg = 'There are products that depend on this brand'
        brand = models.Brands.objects.get(id = brand_id)
        brand.delete()
        result.is_success = True
        result.data = brand
        result.msg = 'Brand Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting Brand.\nError Message: {e}'
    finally:
        return result
#endregion

#region 