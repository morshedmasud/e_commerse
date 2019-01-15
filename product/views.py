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


def product_list(request, cat_coll, cat_name):
    collections = models.Collection.objects.all()
    categorys = models.ProductCategory.objects.all()
    products = models.Products.objects.filter(for_people__title=cat_coll).filter(category__title=cat_name)

    context = {
        "collections": collections,
        "categorys": categorys,
        "products": products,
        "product_title": cat_name
    }
    return render(request, 'products/product_list.html', context)
