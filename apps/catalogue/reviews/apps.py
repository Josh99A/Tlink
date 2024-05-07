import oscar.apps.catalogue.reviews.apps as apps
from django.urls import path


class CatalogueReviewsConfig(apps.CatalogueReviewsConfig):
    name = 'apps.catalogue.reviews'

    def ready(self, *args, **kwargs):
        from .views import CreateProductReview, ProductReviewDetail, ProductReviewList

        self.create_review = CreateProductReview
        self.detail_view = ProductReviewDetail
        self.list_view = ProductReviewList
        
        super().ready(*args, **kwargs)

    def get_urls(self, *args, **kwargs):
        urls = [ 
            path("<int:pk>/", self.detail_view.as_view(), name="reviews-detail"),
            path("add/", self.create_review.as_view(), name="reviews-add"),
            path("", self.list_view.as_view(), name="reviews-list"),

        ] + super().get_urls(*args, **kwargs)

        return self.post_process_urls(urls)
