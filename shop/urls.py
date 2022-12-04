from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('shop/', shop, name='shop'),
    path('delivery/', delivery, name='delivery'),
    path('about_us/', about_us, name='about_us'),
    path('contacts/', contacts, name='contacts'),
    path('shop/<slug:slug>', CategoryDetail.as_view(), name='Category'),
    path('shop/<int:pk>', ProductDetail.as_view(), name='Product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
