from oscar.apps.catalogue.views import ProductDetailView as OscarProductDetailView, ProductCategoryView as OscarProductCategoryView
from store.models import Store

from core.mixins import BaseContextMixin


class ProductCategoryView(BaseContextMixin,OscarProductCategoryView):
    template_name = 'core/Catalogue/browse.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['stores'] = Store.objects.filter(product_type=context['category'].get_root())
        return context


class ProductDetailView(BaseContextMixin, OscarProductDetailView):
    template_name = 'oscar/dashboard/catalogue/product_detail.html'