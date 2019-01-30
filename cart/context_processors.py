from .cart import Cart


def cart(request):
    t = Cart(request)
    print(t.get_total_price())
    return {'cart': Cart(request)}