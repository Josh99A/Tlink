from email import errors
from oscar.apps.catalogue.reviews.forms import ProductReviewForm as OscarProductReviewForm


class ProductReviewForm(OscarProductReviewForm):

    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['score'].widget.attrs.update({'class': 'form-select d-none'})
        if self.errors:
            print(self.errors)
            
            

    class Meta(OscarProductReviewForm.Meta):
        pass