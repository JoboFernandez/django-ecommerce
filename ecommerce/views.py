from django.shortcuts import render

from orders.models import Product, Order


def index(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
    else:
        order = {"item_count": 0}
    discounted_products = Product.objects.filter(discount__gt=0).order_by('-discount')[:4]
    new_arrival_products = Product.objects.order_by('-date_added')[:4]

    context = {
        "order": order,
        "discounted_products": discounted_products,
        "new_arrival_products": new_arrival_products,
    }

    return render(request, 'index.html', context)

