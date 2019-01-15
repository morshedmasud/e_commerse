from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("shop/<cat_coll>/<cat_name>/", views.product_list, name='product_list')
]
