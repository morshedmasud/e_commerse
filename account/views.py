from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import RegistrationForm, ProfileEditForm, UserEditForm



# Create your views here.

def get_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('product:home')
        else:
            messages.error(request, 'username or password mismatch')
            return redirect('account:login')
    else:
        return render(request, 'accounts/login.html')


def get_logout(request):
    logout(request)
    return redirect('product:home')


def get_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user, phone=form.cleaned_data['phone'])
            return redirect('account:login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


@login_required
def user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)



@login_required
def edit_profile(request):
    if request.method == "POST":
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('product:home')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'accounts/edit_profile.html', context)

