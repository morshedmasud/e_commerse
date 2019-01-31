from .models import Collection, ProductCategory


def navbar(request):
    collections = Collection.objects.all()
    categorys = ProductCategory.objects.all()
    for i in categorys:
        print(i.which_people)
    return {'collectios': collections,
            'categorys': categorys}