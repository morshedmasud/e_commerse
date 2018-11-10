from django.contrib import admin
from .models import ProductCategory, Collection, Brand, Size, Color, Products, Image
# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'for_people', 'category', 'price', 'input_date']

    class Meta:
        Model = Products


admin.site.register(Products, ProductAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image']


admin.site.register(Image, ImageAdmin)

