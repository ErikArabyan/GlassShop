from django.urls import path
from .views import *


urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about/', about.as_view(), name='about'),
    path('glasses/', glasses.as_view(), name='glasses'),
    path('shop/', shop.as_view(), name='shop'),
]