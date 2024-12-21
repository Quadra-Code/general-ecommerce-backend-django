from django.urls import path
from core import views as CoreViews
urlpatterns = [
    path('home-api', CoreViews.home, name='home_api')
]