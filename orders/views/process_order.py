from django.http import JsonResponse
import datetime
import json

from ..models import Order, ShippingAddress


def process_order(request):
    data = json.loads(request.body)
    transaction_id = datetime.datetime.now().timestamp()
    order, created = Order.objects.get_or_create(customer=request.user, ordered=False)
    order.transaction_id = transaction_id

    if float(data["shippingInfo"]["total"]) == float(order.total):
        order.ordered = True
        ShippingAddress.objects.create(
            customer=request.user,
            order=order,
            address=data["shippingInfo"]["address"],
            city=data["shippingInfo"]["city"],
            state=data["shippingInfo"]["state"],
            zipcode=data["shippingInfo"]["zipcode"],
        )

    order.save()

    return JsonResponse("Payment complete!", safe=False)