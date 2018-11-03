from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all()
    return render(request, 'base.html', {'products': products})


# def product_list(request):
