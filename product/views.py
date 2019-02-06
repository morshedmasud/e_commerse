from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from . import models
from cart.forms import CartAddProductForm
# Create your views here.


def index(request):
    images = models.Image.objects.all()
    brands = models.Brand.objects.all()
    products = models.Products.objects.all()
    context = {
        "images": images,
        "brands": brands,
        "products": products,
    }
    return render(request, 'products/index.html', context)


def get_search(request):
    brands = models.Brand.objects.all()
    search = request.GET.get('q')
    products = models.Products.objects.filter(
        Q(name__icontains=search) |
        Q(description__icontains=search) |
        Q(category__title__icontains=search) |
        Q(brand__name__icontains=search)
    )
    # paginator = Paginator(products, 1)  # show 6 products in one page
    # page = request.GET.get('page')
    # products_ = paginator.get_page(page)
    context = {
        'products': products,
        'brands': brands
    }
    return render(request, 'products/search_page.html', context)


def product_list(request, cat_coll, cat_name):
    products = models.Products.objects.filter(for_people__title=cat_coll).filter(category__title=cat_name)
    brands = models.Brand.objects.filter(products__category__title=cat_name)
    paginator = Paginator(products, 6) # show 6 products in one page
    page = request.GET.get('page')
    products_ = paginator.get_page(page)

    context = {
        "products": products_,
        "product_category": cat_name,
        "brands": brands,
        "category_for": cat_coll,
    }
    return render(request, 'products/product_list.html', context)


def brand_products(request, brand_name):
    brands = models.Brand.objects.all()
    products = models.Products.objects.filter(brand__name=brand_name)
    paginator = Paginator(products, 10)  # show 6 products in one page
    page = request.GET.get('page')
    products_ = paginator.get_page(page)

    context = {
        "products": products_,
        "brands": brands,
        "brand_name": brand_name
    }
    return render(request, 'products/product_list.html', context)


def single_products(request, id, slug):
    product = get_object_or_404(models.Products, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        "product": product,
        "cart_product_form": cart_product_form
    }
    return render(request, 'products/single-product-details.html', context)
