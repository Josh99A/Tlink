from django.urls import path

from . import views

app_name='store'
urlpatterns = [
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('change-profile-format/', views.ProfileImageView.as_view(), name='profile'),
    path('update-profile/', views.UpdateProfileImageView.as_view(), name='update')
]