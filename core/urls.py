from django.urls import path, re_path

from . import views
from apps.dashboard.catalogue.views import TlinkProductCreateUpdateView

app_name='core'
urlpatterns = [
    path('', views.indexList.as_view() , name='index'),
    path('fashion/', views.FashionCategory.as_view(), name='fashion'),
    path('subscribe/', views.Subscribe.as_view(), name='subscribe'),
    path('<str:subscription>/<str:payment_method>/signup', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/store', views.UserStoreView.as_view(), name='store'),
    re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                TlinkProductCreateUpdateView.as_view(),
                name="catalogue-product-create",
            ),
]