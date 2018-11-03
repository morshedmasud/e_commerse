from django.shortcuts import render
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all().reverse()
    context = {
        "products": products,

    }
    return render(request, 'products/index.html', context)


# def product_list(request):
