from .models import Collection, ProductCategory, Products


def navbar(request):
    categorys = ProductCategory.objects.all()
    collections = Collection.objects.all()
    return {'categorys': categorys,
            'collections': collections}