from django.views.generic import ListView
from django.db.models import Q

from ..models import Product, Category, Order
from ..utils import get_category_filters


class ProductListView(ListView):
    template_name = "orders/product_list.html"
    model = Product
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        sort = self.request.GET.get('sort')
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["query"] = self.request.GET.get('query')
        context["category_filters"] = get_category_filters(request=self.request)
        context["sort"] = sort if sort else '-discounted_price'
        if self.request.user.is_authenticated:
            context["order"] = Order.objects.get(customer=self.request.user, ordered=False)
        else:
            context["order"] = {"item_count": 0}
        return context

    def get_queryset(self):
        query = self.request.GET.get('query')
        category_filters = get_category_filters(request=self.request)
        sort = self.request.GET.get('sort')
        sort = sort if sort else '-discounted_price'
        queryset = Product.objects.all()

        if query and query != "None":
            queryset = queryset.filter(
                Q(name__icontains=query)
            )

        if category_filters:
            queryset = queryset.filter(category__name__in=category_filters)

        if sort == "discounted_price":
            queryset = sorted(queryset, key=lambda product: product.discounted_price)
        elif sort == "-discounted_price":
            queryset = sorted(queryset, key=lambda product: product.discounted_price, reverse=True)
        else:
            queryset = queryset.order_by(sort)

        return queryset
