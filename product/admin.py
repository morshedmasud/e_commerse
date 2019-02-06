from django.contrib import admin
from .models import ProductCategory, Collection, Brand, Size, Color, Products, Image
# Register your models here.


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['which_people', 'title']


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Collection)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'image']


admin.site.register(Image, ImageAdmin)


class ProductImageInline(admin.TabularInline):
    model = Image
    extra = 2


class ProductSizeInline(admin.TabularInline):
    model = Size
    extra = 3


class ProductColorAdmin(admin.TabularInline):
    model = Color
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'stock', 'available', 'for_people', 'category', 'price', 'input_date']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ProductSizeInline, ProductColorAdmin]

    class Meta:
        Model = Products


admin.site.register(Products, ProductAdmin)




