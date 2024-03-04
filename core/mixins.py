from apps.catalogue.models import Category

class CategoryDetailMixin:
    model=Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return  context