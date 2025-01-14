from django.urls import path
from users import views as UserViews
urlpatterns = [
    path('register', UserViews.register, name='register'),
    path('login', UserViews.login_user, name='login'),
    # path('admin/login', UserViews.login_admin, name='login_admin'),
    # path('logout', UserViews.test_sms, name='update_brands'),
    # path('delete-brands/<int:brand_id>', UserViews.delete_brand, name='delete_brands'),
]