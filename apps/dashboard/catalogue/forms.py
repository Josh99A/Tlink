from oscar.apps.dashboard.catalogue.forms import ProductForm as OscarProductForm, ProductClassForm as OscarProductClassForm
from oscar.apps.dashboard.catalogue.forms import StockRecordForm as OscarStockRecordForm


from apps.catalogue.models import Product,  ProductClass



class StockRecordForm(OscarStockRecordForm):
    class Meta(OscarStockRecordForm.Meta):
      pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['partner'].widget.attrs.update({'class':'form-select'})
        self.fields['partner_sku'].widget.attrs.update({'class':'form-control'})
        self.fields['price_currency'].widget.attrs.update({'class':'form-control'})
        self.fields['price'].widget.attrs.update({'class':'form-control'})
        self.fields['num_in_stock'].widget.attrs.update({'class':'form-control'})
        self.fields['low_stock_threshold'].widget.attrs.update({'class':'form-control'})


class ProductForm(OscarProductForm):
    class Meta(OscarProductForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['upc'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control', 'cols':40, 'rows': 5, 'placeholder':'Give a product description'})

class ProductClassForm(OscarProductClassForm):
    class Meta(OscarProductClassForm.Meta):
        model = ProductClass
        fields = ["name", "category", "requires_shipping", "track_stock", "options"]
    
    