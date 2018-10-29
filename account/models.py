from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(upload_to='customer_pic/', null=True, blank=True)
