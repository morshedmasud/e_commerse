from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from account.models import Profile
from .random_num import randomStringNumber


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        user = get_object_or_404(Profile, user=request.user.id)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_order = user
            order.order_number = randomStringNumber()
            order = form.save()
            print('masud')
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            # clear cart
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    context = {
        'cart': cart,
        'form': form
    }

    return render(request, 'order/create.html', context)
