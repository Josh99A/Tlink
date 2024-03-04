from oscar.apps.catalogue.views import ProductDetailView as OscarProductDetailView, ProductCategoryView as OscarProductCategoryView

class ProductCategoryView(OscarProductCategoryView):
    template_name = 'core/Catalogue/browse.html'

    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context


class ProductDetailView(OscarProductDetailView):
    template_name = 'oscar/dashboard/catalogue/product_detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)

        return context