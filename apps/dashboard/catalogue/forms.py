from oscar.apps.dashboard.catalogue.forms import ProductForm as OscarProductForm

from apps.catalogue.models import Product

class ProductForm(OscarProductForm):
    model = Product
    
    