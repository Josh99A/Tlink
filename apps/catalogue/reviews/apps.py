import oscar.apps.catalogue.reviews.apps as apps
from django.urls import path


class CatalogueReviewsConfig(apps.CatalogueReviewsConfig):
    name = 'apps.catalogue.reviews'

    def ready(self, *args, **kwargs):
        from .views import CreateProductReview

        self.create_review = CreateProductReview
        super().ready(*args, **kwargs)

    def get_urls(self, *args, **kwargs):
        urls = [ 
            path("add/", self.create_review.as_view(), name="reviews-add"),

        ] + super().get_urls(*args, **kwargs)

        return self.post_process_urls(urls)
