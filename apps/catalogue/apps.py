import oscar.apps.catalogue.apps as apps
from django.urls import re_path


class CatalogueConfig(apps.CatalogueConfig):
    name = 'apps.catalogue'

    def ready(self,*args, **kwargs):
        from .views import ProductDetailView

        self.detail_view = ProductDetailView
        super().ready()

    def get_urls(self):
        urls = [
             re_path(
                r"^(?P<product_slug>[\w-]*)_(?P<pk>\d+)/$",
                self.detail_view.as_view(),
                name=" detail",
            ),
        ]+ super().get_urls()
    
        return self.post_process_urls(urls)