from django.urls import path

from . import views

app_name='store'
urlpatterns = [
    path('settings/', views.SettingsView.as_view(), name='settings')
]