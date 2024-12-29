from django.urls import path
from users import views as UserViews
urlpatterns = [
    path('register', UserViews.register, name='register'),
    # path('login', UserViews.login, name='login'),
    # path('logout', User.update_brand, name='update_brands'),
    # path('delete-brands/<int:brand_id>', User.delete_brand, name='delete_brands'),
]