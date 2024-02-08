from oscar.apps.customer.views import AccountAuthView as OscarAccountAuthView, LogoutView as OscarLogoutView

from .forms import EmailAuthenticationForm
from django.urls import reverse



class AccountAuthView(OscarAccountAuthView):
    login_form_class = EmailAuthenticationForm


    def get_login_success_url(self, *args, **kwargs):
    
        if self.request.user.is_staff:
            return reverse("store:settings", kwargs={'pk': self.request.user.shop.pk, 'slug':self.request.user.shop.get_slug() })

        return super().get_login_success_url(*args, **kwargs)
    


class LogoutView(OscarLogoutView):
    url = '/'
    