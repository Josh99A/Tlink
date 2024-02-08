from django.urls import path, re_path

from . import views
from apps.dashboard.catalogue import views as  OscarViews

app_name='store'
urlpatterns = [
    path('<int:pk>/settings/', views.SettingsView.as_view(), name='settings'),
    path('<int:pk>/dashboard/', views.DashBoardView.as_view(), name='dashboard'),
    path('product_addition/<str:category>/', views.ProductCreation.as_view(), name='add_product'),
    path('<int:pk>/<slug:slug>/store', views.StoreView.as_view(), name='store'),
    path('upload-profile-image/', views.UploadProfileImageView.as_view(), name='profile_upload'),
    path('<int:pk>/comment-on-store/<slug:slug>/', views.StoreCommentView.as_view(), name="comment"),
    path('<int:pk>/create/store/settings', views.StoreCreationView.as_view(),  name="createStore"),
    re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                OscarViews.TlinkProductCreateUpdateView.as_view(),
                name="product_create",
            ),
]