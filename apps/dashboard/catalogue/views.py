from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView 
from .forms import ProductForm


class TlinkProductCreateUpdateView(ProductCreateUpdateView):
    template_name = "oscar/dashboard/catalogue/product_update.html"
    form_class = ProductForm


    def form_valid(self, form ,*args, **kwargs):
        print("Form is valid")
        form.instance.seller = self.request.user

        response = super().form_valid(form, *args, **kwargs)

        return response