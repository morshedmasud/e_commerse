from django.shortcuts import render, HttpResponse, redirect
from . import models
# Create your views here.


def index(request):
    collections = models.Collection.objects.all()
    categorys = models.ProductCategory.objects.all()
    images = models.Image.objects.all()
    brand = models.Brand.objects.all()
    products = models.Products.objects.all()

    context = {
        "collections": collections,
        'categorys': categorys,
        "images": images,
        "brand": brand,
        "products": products,
    }
    return render(request, 'products/index.html', context)


def product_list(request, cat_name, cat_coll):
    collections = models.Collection.objects.all()
    categorys = models.ProductCategory.objects.all()

    products = models.Products.objects.filter(size=1)

    print("category name--- ", cat_name)
    print("Which People--- ", cat_coll)
    print("All product--- ", products)

    context = {
        "collections": collections,
        "categorys": categorys
    }
    return render(request, 'products/product_list.html', context)
