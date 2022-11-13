from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_main, name='blog_main'),
]
