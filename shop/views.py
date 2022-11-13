from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def shop(request):
    return render(request, 'shop/shop.html')


def contacts(request):
    return render(request, 'contacts.html')


def delivery(request):
    return render(request, 'delivery.html')


def about_us(request):
    return render(request, 'about_us.html')
