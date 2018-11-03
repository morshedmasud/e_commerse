from django.contrib import admin
from .models import ProductCategory, Collection, Brand, Size, Color, Products
# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'for_people', 'category', 'image', 'price', 'input_date']

    class Meta:
        Model = Products


admin.site.register(Products, ProductAdmin)

