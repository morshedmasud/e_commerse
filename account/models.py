from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=300, null=True, blank=True)
    phone = models.DecimalField(null=True, blank=True, max_digits=30, decimal_places=0)
    photo = models.ImageField(upload_to='userProfile/', null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return 'Profile of user {}'.format(self.user.username)