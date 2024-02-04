from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView , ProductClassCreateView as OscarProductClassCreateView

from .forms import ProductForm, ProductClassForm


class TlinkProductCreateUpdateView(ProductCreateUpdateView):
    template_name = "oscar/dashboard/catalogue/product_update.html"
    form_class = ProductForm


    def form_valid(self, form ,*args, **kwargs):
        form.instance.seller = self.request.user

        response = super().form_valid(form, *args, **kwargs)

        return response
    
class ProductClassCreateView(OscarProductClassCreateView):
    form_class= ProductClassForm
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

