from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
