from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('shop/', shop, name='shop'),
    path('delivery/', delivery, name='delivery'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
]
