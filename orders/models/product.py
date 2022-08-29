from django.db import models
from django.urls import reverse

from . import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    details = models.TextField(default="")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    image = models.ImageField(default="no-image-available-1.jpg", upload_to="products")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def discounted_price(self):
        if self.discount:
            return round(float(self.price) * float(100 - self.discount) / 100, 2)
        else:
            return self.price

    def get_absolute_url(self):
        return reverse("orders:detail", kwargs={"pk": self.pk})