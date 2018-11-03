from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    profile_pic = models.ImageField(upload_to='customer_img/%Y/%m/%D/', null=True, blank=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

