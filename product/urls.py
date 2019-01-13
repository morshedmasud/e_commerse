from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("shop/<cat_name>/<cat_coll>/", views.product_list, name='product_list')
]
