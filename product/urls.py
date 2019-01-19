from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("shop/<cat_coll>/<cat_name>/", views.product_list, name='product_list'),
    path("search/", views.get_search, name='get_search'),
    path("brand/<brand_name>", views.brand_products, name='brand'),
    path("single-item/<int:id>/", views.single_products, name='single-item')
]
