from django.http import JsonResponse
import json

from ..models import Product, Order, OrderItem


def update_cart(request):
    data = json.loads(request.body)
    product_id = data["productId"]
    action = data["action"]

    user = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=user, ordered=False)
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "remove":
        order_item.delete()
    else:
        if action == "add":
            order_item.quantity += 1
        elif action == "subtract":
            order_item.quantity -= 1
        order_item.save()

        if order_item.quantity <= 0:
            order_item.delete()

    return JsonResponse("Item was added", safe=False)

