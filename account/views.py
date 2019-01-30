from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from shopping_cart.models import Order
# from .models import Profile


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username, password)
        if user:
            return redirect('home')
        else:
            messages.error(request, 'username or password mismatch')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# def my_profile(request):
#     my_user_profile = Profile.objects.filter(user=request.user).first()
#     my_order = Order.objects.filter(is_ordered=True, owner=my_user_profile)
#     context = {
#         'my_order': my_order
#     }
#
#     return render(request, "accounts/profile.html", context)
