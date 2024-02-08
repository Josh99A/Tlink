from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView , ProductClassCreateView as OscarProductClassCreateView

from .forms import ProductForm, ProductClassForm
from .formsets import StockRecordFormSet


class TlinkProductCreateUpdateView(ProductCreateUpdateView):
    # template_name = "oscar/dashboard/catalogue/product_update.html"
    template_name = "store/dashboard/product_addition.html"
    form_class = ProductForm
    stockrecord_formset = StockRecordFormSet

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formsets = {
            "category_formset": self.category_formset,
            "image_formset": self.image_formset,
            "recommended_formset": self.recommendations_formset,
            "stockrecord_formset": self.stockrecord_formset,
        }


    def form_valid(self, form ,*args, **kwargs):
        form.instance.seller = self.request.user
         

        response = super().form_valid(form, *args, **kwargs)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
        
class ProductClassCreateView(OscarProductClassCreateView):
    form_class= ProductClassForm
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

