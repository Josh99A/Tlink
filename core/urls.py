from django.urls import path, re_path, reverse


from . import views
from apps.dashboard.catalogue.views import TlinkProductCreateUpdateView

app_name='core'
urlpatterns = [
    path('', views.indexList.as_view() , name='index'),
    path('subscribe/', views.Subscribe.as_view(), name='subscribe'),
    re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                TlinkProductCreateUpdateView.as_view(),
                name="catalogue-product-create",
            ),
]