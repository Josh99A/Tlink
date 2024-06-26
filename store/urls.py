from django.urls import path, re_path

from . import views
from apps.dashboard.catalogue import views as  OscarViews

app_name='store'
urlpatterns = [
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('settings/store/update', views.StoreCreationView.as_view(), name='updateStore'),
    path('profile/update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
    path('profile/change_password/', views.ChangePasswordView.as_view(), name='change-password'),
    path('<int:pk>/follow/store/', views.FollowView.as_view(), name='follow'),
    path('<int:pk>/dashboard/', views.DashBoardView.as_view(), name='dashboard'),
    path('product_addition/<str:category>/', views.ProductCreation.as_view(), name='add_product'),
    path('<int:pk>/<slug:slug>/store', views.StoreView.as_view(), name='store'),
    path('upload-profile-image/', views.UploadProfileImageView.as_view(), name='profile_upload'),
    path('filter/products_by/<str:product_class>/<int:pk>/<slug:slug>', views.ProductClassFilterView.as_view(), name='productclass'),
    path('<int:pk>/<slug:slug>/comment-on-store/', views.StoreCommentView.as_view(), name="comment"),
    path('<int:pk>/vote/comment', views.AddVoteView.as_view() , name='add-vote'),
    path('<int:comment_pk>/reply/comment', views.CommentReplyView.as_view(), name='reply'),
    path('create/store/settings', views.StoreCreationView.as_view(),  name="createStore"),
    re_path(
                r"^products/create/(?P<product_class_slug>[\w-]+)/$",
                OscarViews.TlinkProductCreateUpdateView.as_view(),
                name="product_create",
            ),
   
]