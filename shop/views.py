from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from shop.models import *


def index(request):
    r_cat = Category.objects.order_by('?')[:3]
    return render(request, 'index.html', {'r_cat': r_cat})


def shop(request):
    category = Category.objects.all()
    return render(request, 'shop/shop.html', {'category': category})


def contacts(request):
    return render(request, 'contacts.html')


def delivery(request):
    return render(request, 'delivery.html')


def about_us(request):
    return render(request, 'about_us.html')


class CategoryDetail(generic.DetailView):
    model = Category


class ProductDetail(generic.DetailView):
    model = Product
