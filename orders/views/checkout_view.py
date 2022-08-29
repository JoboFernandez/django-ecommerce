from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models import Order


@login_required
def checkout_view(request):
    user = request.user
    order, created = Order.objects.get_or_create(customer=user, ordered=False)
    order_items = order.orderitem_set.all()

    context = {
        "order": order,
        "order_items": order_items,
    }

    return render(request, "orders/checkout.html", context)

