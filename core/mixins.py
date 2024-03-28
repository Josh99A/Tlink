from apps.catalogue.models import Category
from django.conf import settings

class BaseContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_categories = Category.objects.filter(depth=1)
        context['base_categories'] = base_categories
        context['site_name'] = settings.SITE_NAME
        context['site_name_short'] = settings.SITE_NAME_SHORT
        return  context