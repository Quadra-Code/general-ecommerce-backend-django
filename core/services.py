from django.core.exceptions import ObjectDoesNotExist
from core import models
from core import serializers
from core.base_models import ResultView
# Create your services here.

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
        if models.Products.objects.filter(brand_id=brand_id).exists():
            result.msg = 'There are products that depend on this brand'
        else:
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

#region Coupon Region
def get_all_coupons():
    result = ResultView()
    try:
        all_coupons = models.Coupons.objects.all()
        serialized_coupons = serializers.CouponSerializer(all_coupons, many=True)
        result.is_success = True
        result.data = serialized_coupons.data
        result.msg = 'All Coupons Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All Coupons.\nError Message: {e}'
    finally:
        return result

def create_coupon(request_data):
    result = ResultView()
    try:
        serialized_new_coupon = serializers.CouponSerializer(data=request_data)
        if serialized_new_coupon.is_valid():
            serialized_new_coupon.save()
            result.is_success = True
            result.data = serialized_new_coupon.data
            result.msg = 'New Coupon Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New Coupon.\nError Message: {serialized_new_coupon.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New Coupon.\nError Message: {e}'
    finally:
        return result

def update_coupon(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_coupon = models.Coupons.objects.get(id=request_data.id)
            serialized_updated_coupon = serializers.CouponSerializer(old_coupon, data=request_data)
            if serialized_updated_coupon.is_valid():
                serialized_updated_coupon.save()
                result.is_success = True
                result.data = serialized_updated_coupon.data
                result.msg = 'Coupon Updated Successfully'
            else:
                result.msg = f'New Updated Coupon Data Is Not Valid.\nError Message: {serialized_updated_coupon.errors}'
        else:
            result.msg = f'There is no Coupon id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating Coupon.\nError Message: {e}'
    finally:
        return result

def delete_coupon(coupon_id):
    result = ResultView()
    try:
      coupon = models.Coupons.objects.get(id = coupon_id)
      coupon.delete()
      result.is_success = True
      result.data = coupon
      result.msg = 'Coupon Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting Coupon.\nError Message: {e}'
    finally:
        return result
#endregion

#region Size Region
def get_all_sizes():
    result = ResultView()
    try:
        all_sizes = models.Sizes.objects.all()
        serialized_sizes = serializers.SizeSerializer(all_sizes, many=True)
        result.is_success = True
        result.data = serialized_sizes.data
        result.msg = 'All sizes Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All sizes.\nError Message: {e}'
    finally:
        return result

def create_size(request_data):
    result = ResultView()
    try:
        serialized_new_size = serializers.SizeSerializer(data=request_data)
        if serialized_new_size.is_valid():
            serialized_new_size.save()
            result.is_success = True
            result.data = serialized_new_size.data
            result.msg = 'New size Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New size.\nError Message: {serialized_new_size.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New size.\nError Message: {e}'
    finally:
        return result

def update_size(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_size = models.Sizes.objects.get(id=request_data.id)
            serialized_updated_size = serializers.SizeSerializer(old_size, data=request_data)
            if serialized_updated_size.is_valid():
                serialized_updated_size.save()
                result.is_success = True
                result.data = serialized_updated_size.data
                result.msg = 'size Updated Successfully'
            else:
                result.msg = f'New Updated size Data Is Not Valid.\nError Message: {serialized_updated_size.errors}'
        else:
            result.msg = f'There is no size id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating size.\nError Message: {e}'
    finally:
        return result

def delete_size(size_id):
    result = ResultView()
    try:
      size = models.Sizes.objects.get(id = size_id)
      size.delete()
      result.is_success = True
      result.data = size
      result.msg = 'size Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting size.\nError Message: {e}'
    finally:
        return result
#endregion

#region OrderState Region
def get_all_orderStates():
    result = ResultView()
    try:
        all_orderStates = models.OrderStates.objects.all()
        serialized_orderStates = serializers.OrderStateSerializer(all_orderStates, many=True)
        result.is_success = True
        result.data = serialized_orderStates.data
        result.msg = 'All orderStates Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All orderStates.\nError Message: {e}'
    finally:
        return result

def create_orderState(request_data):
    result = ResultView()
    try:
        serialized_new_orderState = serializers.OrderStateSerializer(data=request_data)
        if serialized_new_orderState.is_valid():
            serialized_new_orderState.save()
            result.is_success = True
            result.data = serialized_new_orderState.data
            result.msg = 'New orderState Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New orderState.\nError Message: {serialized_new_orderState.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New orderState.\nError Message: {e}'
    finally:
        return result

def update_orderState(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_orderState = models.OrderStates.objects.get(id=request_data.id)
            serialized_updated_orderState = serializers.OrderStateSerializer(old_orderState, data=request_data)
            if serialized_updated_orderState.is_valid():
                serialized_updated_orderState.save()
                result.is_success = True
                result.data = serialized_updated_orderState.data
                result.msg = 'orderState Updated Successfully'
            else:
                result.msg = f'New Updated orderState Data Is Not Valid.\nError Message: {serialized_updated_orderState.errors}'
        else:
            result.msg = f'There is no orderState id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating orderState.\nError Message: {e}'
    finally:
        return result

def delete_orderState(orderState_id):
    result = ResultView()
    try:
      orderState = models.OrderStates.objects.get(id = orderState_id)
      orderState.delete()
      result.is_success = True
      result.data = orderState
      result.msg = 'orderState Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting orderState.\nError Message: {e}'
    finally:
        return result
#endregion

#region Extra Region
def get_all_extras():
    result = ResultView()
    try:
        all_extras = models.Extras.objects.all()
        serialized_extras = serializers.ExtraSerializer(all_extras, many=True)
        result.is_success = True
        result.data = serialized_extras.data
        result.msg = 'All extras Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All extras.\nError Message: {e}'
    finally:
        return result

def create_extra(request_data):
    result = ResultView()
    try:
        serialized_new_extra = serializers.ExtraSerializer(data=request_data)
        if serialized_new_extra.is_valid():
            serialized_new_extra.save()
            result.is_success = True
            result.data = serialized_new_extra.data
            result.msg = 'New extra Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New extra.\nError Message: {serialized_new_extra.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New extra.\nError Message: {e}'
    finally:
        return result

def update_extra(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_extra = models.Extras.objects.get(id=request_data.id)
            serialized_updated_extra = serializers.ExtraSerializer(old_extra, data=request_data)
            if serialized_updated_extra.is_valid():
                serialized_updated_extra.save()
                result.is_success = True
                result.data = serialized_updated_extra.data
                result.msg = 'extra Updated Successfully'
            else:
                result.msg = f'New Updated extra Data Is Not Valid.\nError Message: {serialized_updated_extra.errors}'
        else:
            result.msg = f'There is no extra id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating extra.\nError Message: {e}'
    finally:
        return result

def delete_extra(extra_id):
    result = ResultView()
    try:
      extra = models.Extras.objects.get(id = extra_id)
      extra.delete()
      result.is_success = True
      result.data = extra
      result.msg = 'extra Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting extra.\nError Message: {e}'
    finally:
        return result
#endregion

#region category Region
def get_all_categories():
    result = ResultView()
    try:
        all_categories = models.Categories.objects.all()
        serialized_categories = serializers.CategorySerializer(all_categories, many=True)
        result.is_success = True
        result.data = serialized_categories.data
        result.msg = 'All categories Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All categories.\nError Message: {e}'
    finally:
        return result

def create_category(request_data):
    result = ResultView()
    try:
        serialized_new_category = serializers.CategorySerializer(data=request_data)
        if serialized_new_category.is_valid():
            serialized_new_category.save()
            result.is_success = True
            result.data = serialized_new_category.data
            result.msg = 'New category Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New category.\nError Message: {serialized_new_category.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New category.\nError Message: {e}'
    finally:
        return result

def update_category(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_category = models.Categories.objects.get(id=request_data.id)
            serialized_updated_category = serializers.CategorySerializer(old_category, data=request_data)
            if serialized_updated_category.is_valid():
                serialized_updated_category.save()
                result.is_success = True
                result.data = serialized_updated_category.data
                result.msg = 'category Updated Successfully'
            else:
                result.msg = f'New Updated category Data Is Not Valid.\nError Message: {serialized_updated_category.errors}'
        else:
            result.msg = f'There is no category id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating category.\nError Message: {e}'
    finally:
        return result

def delete_category(category_id):
    result = ResultView()
    try:
        # here we can check if there is any related entities (products) if the business logic requires the category field not to be null
        # else we can delete and the models on delete will set the field to null
        if models.Products.objects.filter(category_id=category_id).exists():
            result.msg = 'There are products that depend on this category'
        else:
            category = models.Categories.objects.get(id = category_id)
            category.delete()
            result.is_success = True
            result.data = category
            result.msg = 'category Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting category.\nError Message: {e}'
    finally:
        return result
#endregion

#region City Region
def get_all_cities():
    result = ResultView()
    try:
        all_cities = models.Cities.objects.all()
        serialized_cities = serializers.CitySerializer(all_cities, many=True)
        result.is_success = True
        result.data = serialized_cities.data
        result.msg = 'All cities Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All cities.\nError Message: {e}'
    finally:
        return result

def create_city(request_data):
    result = ResultView()
    try:
        serialized_new_city = serializers.CitySerializer(data=request_data)
        if serialized_new_city.is_valid():
            serialized_new_city.save()
            result.is_success = True
            result.data = serialized_new_city.data
            result.msg = 'New city Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New city.\nError Message: {serialized_new_city.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New city.\nError Message: {e}'
    finally:
        return result

def update_city(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_city = models.Cities.objects.get(id=request_data.id)
            serialized_updated_city = serializers.CitySerializer(old_city, data=request_data)
            if serialized_updated_city.is_valid():
                serialized_updated_city.save()
                result.is_success = True
                result.data = serialized_updated_city.data
                result.msg = 'city Updated Successfully'
            else:
                result.msg = f'New Updated city Data Is Not Valid.\nError Message: {serialized_updated_city.errors}'
        else:
            result.msg = f'There is no city id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating city.\nError Message: {e}'
    finally:
        return result

def delete_city(city_id):
    result = ResultView()
    try:
      city = models.Cities.objects.get(id = city_id)
      city.delete()
      result.is_success = True
      result.data = city
      result.msg = 'city Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting city.\nError Message: {e}'
    finally:
        return result
#endregion

#region Country Region
def get_all_countries():
    result = ResultView()
    try:
        all_countries = models.Countries.objects.all()
        serialized_countries = serializers.CountrySerializer(all_countries, many=True)
        result.is_success = True
        result.data = serialized_countries.data
        result.msg = 'All countries Fetched & Serialized Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Fetching & Serializing All countries.\nError Message: {e}'
    finally:
        return result

def get_all_countries_cities():
    result = ResultView()
    try:
        # Prefetch related cities using the reverse relation name
        all_countries_cities = models.Countries.objects.prefetch_related('cities').all()
        serialized_countries_cities = serializers.CountryWithCitiesSerializer(all_countries_cities, many=True)
        result.is_success = True
        result.data = serialized_countries_cities.data
        result.msg = 'All countries and their cities fetched successfully'
    except Exception as e:
        result.is_success = False
        result.msg = f'Error occurred while fetching countries and cities. Error: {e}'
    finally:
        return result

def create_country(request_data):
    result = ResultView()
    try:
        serialized_new_country = serializers.CountrySerializer(data=request_data)
        if serialized_new_country.is_valid():
            serialized_new_country.save()
            result.is_success = True
            result.data = serialized_new_country.data
            result.msg = 'New country Created Successfully'
        else:
            result.msg = f'Error Happend While Saving New country.\nError Message: {serialized_new_country.errors}'
    except Exception as e:
        result.msg = f'Error Happened While Creating New country.\nError Message: {e}'
    finally:
        return result

def update_country(request_data):
    result = ResultView()
    try:
        if request_data.id:
            old_country = models.Countries.objects.get(id=request_data.id)
            serialized_updated_country = serializers.CountrySerializer(old_country, data=request_data)
            if serialized_updated_country.is_valid():
                serialized_updated_country.save()
                result.is_success = True
                result.data = serialized_updated_country.data
                result.msg = 'country Updated Successfully'
            else:
                result.msg = f'New Updated country Data Is Not Valid.\nError Message: {serialized_updated_country.errors}'
        else:
            result.msg = f'There is no country id in the recieved data'
    except Exception as e:
        result.msg = f'Error Happened While Updating country.\nError Message: {e}'
    finally:
        return result

def delete_country(country_id):
    result = ResultView()
    try:
        # here we can check if there is any related entities (cities) if the business logic requires the brand field not to be null
        # else we can delete and the models on delete will set the field to null
        if models.Cities.objects.filter(country=country_id).exists():
            result.msg = 'There are cities that depend on this country'
        else:
            country = models.Countries.objects.get(id = country_id)
            country.delete()
            result.is_success = True
            result.data = country
            result.msg = 'country Deleted Successfully'
    except Exception as e:
        result.msg = f'Error Happened While Deleting country.\nError Message: {e}'
    finally:
        return result
#endregion

