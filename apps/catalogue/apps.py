import oscar.apps.catalogue.apps as apps
from django.urls import re_path


class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    def ready(self,*args, **kwargs):
        from .views import ProductDetailView, ProductCategoryView

        self.detail_view = ProductDetailView
        self.category_view = ProductCategoryView
        super().ready(*args, **kwargs)

    def get_urls(self):
        urls = [
             re_path(
                r"^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$",
                self.detail_view.as_view(),
                name=" detail",
            ),
        ] + super().get_urls()
    
        return self.post_process_urls(urls)