from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ['user', 'phone', 'address']


admin.site.register(Profile, ProfileAdmin)

