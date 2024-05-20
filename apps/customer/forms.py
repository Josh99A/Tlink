from oscar.apps.customer.forms import  EmailAuthenticationForm as OscarEmailAuthenticationForm, EmailUserCreationForm as OscarEmailUserCreationForm
from oscar.apps.customer.forms import  UserForm as OscarProfileForm, ConfirmPasswordForm as OscarConfirmPasswordForm
from django import forms
from django.core.exceptions import ValidationError

import re



class ConfirmPasswordForm(OscarConfirmPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'class':'form-select border border-primary-subtle'})

class EmailUserCreationForm(OscarEmailUserCreationForm):
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
    class Meta(OscarEmailUserCreationForm.Meta):
        fields = OscarEmailUserCreationForm.Meta.fields + ('phone_number','first_name', 'whatsApp',  'last_name', 'has_accepted_terms_and_conditions', 'date_of_birth', 'location', 'gender', 'profile_image')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs.update({'class':' w-25 mx-1 my-1 form-select border border-primary-subtle'})
        self.fields['has_accepted_terms_and_conditions'].widget.attrs.update({'class':'form-check-input border border-primary-subtle', 'required': ''})
        self.fields['location'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['gender'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['whatsApp'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['email'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['password1'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['password2'].widget.attrs.update({'class':'form-select border border-primary-subtle'})

    def clean_phone_number(self, *args, **kwargs):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = r'^\+?256[0-9]{9}$'
       
        if not re.match(pattern, phone_number):
            raise ValidationError("Please enter a valid phone number")
        return phone_number
    
    def clean_whatsApp(self, *args, **kwargs):
        whatsApp = self.cleaned_data.get('whatsApp')
        pattern = r'^\+?256[0-9]{9}$'
       
        if not re.match(pattern, whatsApp):
            raise ValidationError("Please enter a valid number format")
        return whatsApp
    
    def clean_has_accepted_terms_and_conditions(self):
        has_accepted_terms_and_conditions =  self.cleaned_data.get('has_accepted_terms_and_conditions')

        if not has_accepted_terms_and_conditions:
            raise ValidationError("Please read and accept the terms and conditions before continuing")
        
        return has_accepted_terms_and_conditions
        


class EmailAuthenticationForm(OscarEmailAuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['password'].widget.attrs.update({'class':'form-control border border-primary-subtle'})


class ProfileForm(OscarProfileForm):
    class Meta(OscarProfileForm.Meta):
        fields = OscarProfileForm.Meta.fields + ['location', 'phone_number', 'whatsApp']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['first_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['phone_number'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['whatsApp'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['email'].widget.attrs.update({'class':'form-control border border-primary-subtle'})