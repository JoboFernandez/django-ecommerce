from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f"{self.customer.username}: {self.transaction_id}"

    @property
    def total(self):
        return sum([item.total for item in self.orderitem_set.all()])

    @property
    def item_count(self):
        return sum([item.quantity for item in self.orderitem_set.all()])