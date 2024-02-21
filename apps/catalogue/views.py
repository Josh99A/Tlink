from oscar.apps.catalogue.views import ProductDetailView as OscarProductDetailView


class ProductDetailView(OscarProductDetailView):
    template_name = 'oscar/dashboard/catalogue/product_detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)

        return context