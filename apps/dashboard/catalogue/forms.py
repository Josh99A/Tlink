from oscar.apps.dashboard.catalogue.forms import ProductForm as OscarProductForm, ProductClassForm as OscarProductClassForm

from apps.catalogue.models import Product,  ProductClass

class ProductForm(OscarProductForm):
    model = Product

class ProductClassForm(OscarProductClassForm):
    class Meta(OscarProductClassForm.Meta):
        model = ProductClass
        fields = ["name", "category", "requires_shipping", "track_stock", "options"]
    
    