from oscar.apps.catalogue.reviews.views import CreateProductReview as OscarCreateProductReview
from core.mixins import BaseContextMixin

class CreateProductReview(BaseContextMixin, OscarCreateProductReview):
    def get_context_data(self,*args, **kwargs):
        
        print('The context' , super().get_context_data(*args, **kwargs))
        return super().get_context_data(*args, **kwargs)