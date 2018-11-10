from django.db import models
from django.utils import timezone


# Create your models here.

class Collection(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class Products(models.Model):
    name = models.CharField(max_length=200)
    for_people = models.ForeignKey(Collection, on_delete=models.CASCADE)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    # image = models.ImageField(upload_to='product_img/')
    old_price = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    input_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name


class Image(models.Model):
    product_name = models.ForeignKey(Products, related_name='pro_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_img/', null=True, blank=True)

    def __str__(self):
        return self.product_name.name + 'image'
