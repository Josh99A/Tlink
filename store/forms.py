from django.forms import ModelForm, CheckboxSelectMultiple
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm as BasePasswordChangeForm
from django.utils.translation import gettext as _

from apps.catalogue.models import Category


from .models import Store, Comment, Vote
from core.models import User


class PasswordChangeForm(BasePasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control border border-primary-subtle'})


class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields = [
            'name', 'location','product_type', 'location_image1',
            'location_image2', 'location_image3',
            'location_image4'
            ]  

        widgets = {
            'product_type': CheckboxSelectMultiple(attrs={'class':'form-check-input border border-primary-subtle'})
        } 

    def __init__(self, *args,**kwargs):
        super().__init__(*args,  **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control border border-primary-subtle'})
        self.fields['location'].widget.attrs.update({'class':'form-select border border-primary-subtle'})
        self.fields['location_image1'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card1', 'imageName1')"})
        self.fields['location_image2'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card2', 'imageName2')"})
        self.fields['location_image3'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card3', 'imageName3')"})
        self.fields['location_image4'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card4', 'imageName4')"})

        # 
        self.fields['product_type'].queryset = Category.objects.filter(depth=1)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'score', 'message' )

    def __init__(self, store=None, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.store = store
        self.user = user
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['score'].widget.attrs.update({'class':'form-control d-none'})
        self.fields['message'].widget.attrs.update({'class':'form-control', 'cols':40, 'rows': 5, 'placeholder':'Enter your comment'})


    def clean(self):
        cleaned_data = super().clean()
        if self.user and self.store:  
            if not self.user.is_authenticated: 
                raise ValidationError(_("Only signed-in users can comment on stores"))
            if  self.store.owner == self.user:
                raise ValidationError(_("You cannot comment on your own store"))
            previous_comments = self.store.comments.filter(user=self.user)
            if len(previous_comments) > 0:
                    raise ValidationError(_("You can only comment once on a store"))

        return cleaned_data



class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ("delta",)

    def __init__(self, comment, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.comment = comment
        self.instance.user = user

    @property
    def is_up_vote(self):
        return self.cleaned_data["delta"] == Vote.UP

    @property
    def is_down_vote(self):
        return self.cleaned_data["delta"] == Vote.DOWN
