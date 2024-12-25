from django.urls import path
from core import views as CoreViews
urlpatterns = [
    path('get-all-brands', CoreViews.get_all_brands, name='get_all_brands'),
    path('create-brands', CoreViews.create_brand, name='create_brands'),
    path('update-brands', CoreViews.update_brand, name='update_brands'),
    path('delete-brands/<int:brand_id>', CoreViews.delete_brand, name='delete_brands'),
]