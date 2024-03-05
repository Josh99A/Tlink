from apps.catalogue.models import Category

class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_categories = Category.objects.filter(depth=1)
        context['base_categories'] = base_categories
        return  context