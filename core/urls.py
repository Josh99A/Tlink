from django.urls import path, re_path, reverse


from . import views
from apps.dashboard.catalogue.views import TlinkProductCreateUpdateView

app_name='core'
urlpatterns = [
    path('', views.indexList.as_view() , name='index'),
    path('fashion/', views.FashionCategory.as_view(), name='fashion'),
    path('subscribe/', views.Subscribe.as_view(), name='subscribe'),
    path('<str:subscription>/<str:payment_method>/signup', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/store', views.UserStoreView.as_view(), name='store'),
<<<<<<< HEAD
=======
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html',)),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/', )),
>>>>>>> c604ec879be2dacb8851f4402cffea54523cb472
    re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                TlinkProductCreateUpdateView.as_view(),
                name="catalogue-product-create",
            ),
]