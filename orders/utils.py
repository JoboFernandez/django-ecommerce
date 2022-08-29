from .models import Category


def get_category_filters(request):
    filters = request.GET.getlist('category')
    if not filters:
        filters = Category.objects.all().values_list('name', flat=True)
    return filters

