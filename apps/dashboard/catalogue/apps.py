import oscar.apps.dashboard.catalogue.apps as apps
from django.urls import re_path, path


class CatalogueDashboardConfig(apps.CatalogueDashboardConfig):
    name = 'apps.dashboard.catalogue'

    def ready(self):
        from .views import TlinkProductCreateUpdateView, ProductClassCreateView
        self.product_createupdateproduct_view = TlinkProductCreateUpdateView
        self.product_class_create_view = ProductClassCreateView
        super().ready()



    def get_urls(self):
        urls = [ 
             path(
                "products/<int:pk>/",
                self.product_createupdateproduct_view.as_view(),
                name="catalogue-product",
            ),
            path(
                "product-type/create/",
                self.product_class_create_view.as_view(),
                name="catalogue-class-create",
            ),
              re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                self.product_createupdateproduct_view.as_view(),
                name="catalogue-product-create",
            ),
        ] + super().get_urls()
        return self.post_process_urls(urls)


