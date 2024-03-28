from django.forms import ModelForm,TextInput, PasswordInput, CharField, ValidationError
from core.models import User

class UserCreationForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput, help_text='Enter the same password as above')
    class Meta:
        model = User
        fields = ( 'email', 'phone_number', 'password','confirm_password', 'gender', 'date_of_birth', 'location', 'profile_image')

        widgets = {
            'password': PasswordInput(attrs={'class': 'has-text-warning'})
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Passwords do not match.')
    