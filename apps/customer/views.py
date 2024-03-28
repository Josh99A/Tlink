from oscar.apps.customer.views import AccountAuthView as OscarAccountAuthView, LogoutView as OscarLogoutView, ChangePasswordView as OscarChangePasswordView, AccountRegistrationView as OscarAccountRegistrationView
from oscar.apps.customer.views import ProfileView as OscarProfileView, ProfileUpdateView as OscarProfileUpdateView, ProfileDeleteView as OscarProfileDeleteView

from .forms import EmailAuthenticationForm, ProfileForm, EmailUserCreationForm
from django.urls import reverse
from core.mixins import BaseContextMixin



class AccountAuthView(BaseContextMixin, OscarAccountAuthView):
    template_name = 'core/login.html'
    login_form_class = EmailAuthenticationForm


    def get_login_success_url(self, *args, **kwargs):
    
        if self.request.user.is_staff:
            return reverse("store:settings")

        return super().get_login_success_url(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        print( super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)
    
class AccountRegistrationView(BaseContextMixin, OscarAccountRegistrationView):
    template_name = 'core/register.html'
    form_class = EmailUserCreationForm

    def get_context_data(self, **kwargs):
        print( super().get_context_data(**kwargs))
        return super().get_context_data(**kwargs)

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



    