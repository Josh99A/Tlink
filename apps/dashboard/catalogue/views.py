from oscar.apps.dashboard.catalogue.views import ProductCreateUpdateView , ProductClassCreateView as OscarProductClassCreateView
from oscar.apps.dashboard.catalogue.views import ProductListView as OscarProductListView

from django.urls import reverse
from django.shortcuts import render

from .forms import ProductForm, ProductClassForm
from .formsets import StockRecordFormSet
from .tables import ProductTable


class ProductListView(OscarProductListView):
    table_class = ProductTable


class TlinkProductCreateUpdateView(ProductCreateUpdateView):
    template_name = "store/dashboard/product_addition.html"
    form_class = ProductForm
    stockrecord_formset = StockRecordFormSet

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formsets = {
            "image_formset": self.image_formset,
            "stockrecord_formset": self.stockrecord_formset,
        }


    def form_valid(self, form ,*args, **kwargs):
        product = form.save(commit=False)
        product.seller = self.request.user
        product.save()
        
        # Add the product to the current user's store
        self.request.user.shop.record.products.add(product)
        product.categories.add(self.get_context_data()['product_class'].category)
    
        response = super().form_valid(form, *args, **kwargs)

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self, **kwargs):
        super().get_success_url(**kwargs)
        action = self.request.POST.get("action")
        if action == "continue":
            url = reverse("dashboard:catalogue-product", kwargs={"pk": self.object.id})
        else:
            url = reverse("store:dashboard", kwargs={'pk':self.request.user.pk})
        return self.get_url_with_querystring(url)

        
class ProductClassCreateView(OscarProductClassCreateView):
    form_class= ProductClassForm
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

