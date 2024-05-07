from oscar.apps.catalogue.reviews.views import CreateProductReview as OscarCreateProductReview, ProductReviewDetail as OscarProductReviewDetail,  ProductReviewList as OscarProductReviewList
from core.mixins import BaseContextMixin
from .forms import ProductReviewForm

class CreateProductReview(BaseContextMixin, OscarCreateProductReview):
    form_class = ProductReviewForm

class ProductReviewDetail(BaseContextMixin, OscarProductReviewDetail):
    pass

class  ProductReviewList(BaseContextMixin, OscarProductReviewList):
    # template_name = 'Oscar/catalogue/partials/review_list.html'
    pass

