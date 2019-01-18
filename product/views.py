from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
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


def get_search(request):
    collections = models.Collection.objects.all()
    categorys = models.ProductCategory.objects.all()
    brands = models.Brand.objects.all()
    search = request.POST.get('s')
    products = models.Products.objects.filter(
        Q(name__icontains=search) |
        Q(description__icontains=search) |
        Q(category__title__icontains=search) |
        Q(brand__name__icontains=search)
    )

    context = {
        "collections": collections,
        'categorys': categorys,
        'products': products,
        'brands': brands
    }
    return render(request, 'products/search_page.html', context)


def product_list(request, cat_coll, cat_name):
    collections = models.Collection.objects.all()
    categorys = models.ProductCategory.objects.all()
    products = models.Products.objects.filter(for_people__title=cat_coll).filter(category__title=cat_name)
    brands = models.Brand.objects.filter(products__category__title=cat_name)

    context = {
        "collections": collections,
        "categorys": categorys,
        "products": products,
        "product_title": cat_name,
        "brands": brands,
        "category_for": cat_coll
    }
    return render(request, 'products/product_list.html', context)
