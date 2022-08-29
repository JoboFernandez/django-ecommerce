from django.views.generic import DetailView

from ..models import Product, Order


class ProductDetailView(DetailView):
    template_name = "orders/product_detail.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["order"] = Order.objects.get(customer=self.request.user, ordered=False)
        else:
            context["order"] = {"item_count": 0}
        return context
