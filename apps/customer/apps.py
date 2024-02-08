import oscar.apps.customer.apps as apps

from django.urls import path, re_path




class CustomerConfig(apps.CustomerConfig):
    name = 'apps.customer'

    def ready(self):
        from .views import AccountAuthView, LogoutView
        self.login_view = AccountAuthView
        self.logout_view = LogoutView

        super().ready()


    def get_urls(self):
        urls = [
            path("login/", self.login_view.as_view(), name="login"),
            path("logout/", self.logout_view.as_view(), name="logout"),

        ] + super().get_urls()
        
        return  self.post_process_urls(urls)

