from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.get_login, name='login'),
    path('logout/', views.get_logout, name='logout'),
    path('registration/', views.get_registration, name='registration'),
    path('profile/', views.user_profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='editProfile')
]