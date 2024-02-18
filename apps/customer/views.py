from oscar.apps.customer.views import AccountAuthView as OscarAccountAuthView, LogoutView as OscarLogoutView, ChangePasswordView as OscarChangePasswordView
from oscar.apps.customer.views import ProfileView as OscarProfileView, ProfileUpdateView as OscarProfileUpdateView, ProfileDeleteView as OscarProfileDeleteView

from .forms import EmailAuthenticationForm, ProfileForm
from django.urls import reverse



class AccountAuthView(OscarAccountAuthView):
    login_form_class = EmailAuthenticationForm


    def get_login_success_url(self, *args, **kwargs):
    
        if self.request.user.is_staff:
            return reverse("store:settings")

        return super().get_login_success_url(*args, **kwargs)
    


class LogoutView(OscarLogoutView):
    url = '/'

class ProfileView(OscarProfileView):
    pass

class ProfileUpdateView(OscarProfileUpdateView):
    form_class = ProfileForm

class ProfileDeleteView(OscarProfileDeleteView):
    pass

class ChangePasswordView(OscarChangePasswordView):
    pass



    