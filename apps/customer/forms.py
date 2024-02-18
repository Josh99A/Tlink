from oscar.apps.customer.forms import  EmailAuthenticationForm as OscarEmailAuthenticationForm
from oscar.apps.customer.forms import  UserForm as OscarProfileForm, ConfirmPasswordForm as OscarConfirmPasswordForm




class ConfirmPasswordForm(OscarConfirmPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class':'form-select border border-primary-subtle'})


class EmailAuthenticationForm(OscarEmailAuthenticationForm):
    pass


class ProfileForm(OscarProfileForm):
    class Meta(OscarProfileForm.Meta):
        fields = OscarProfileForm.Meta.fields + ['location', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['email'].widget.attrs.update({'class':'form-control border border-primary-subtle'})