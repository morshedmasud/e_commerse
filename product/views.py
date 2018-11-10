from django.shortcuts import render
from .models import Products, Image
# Create your views here.


def index(request):
    products = Products.objects.all().reverse()
    images = Image.objects.all()
    context = {
        "products": products,
        "images": images

    }
    return render(request, 'products/index.html', context)


# def product_list(request):
