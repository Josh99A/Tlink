from django.forms import ModelForm, HiddenInput
from django.core.exceptions import ValidationError
from .models import Store, Comment
from core.models import User
from django.utils.translation import gettext as _

class StoreForm(ModelForm):
    class Meta:
        model=Store
        fields = [
            'name', 'location', 'location_image1',
            'location_image2', 'location_image3',
            'location_image4'
            ]   

    def __init__(self, *args,**kwargs):
        super().__init__(*args,  **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['location'].widget.attrs.update({'class':'form-select'})
        self.fields['location_image1'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card1', 'imageName1')"})
        self.fields['location_image2'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card2', 'imageName2')"})
        self.fields['location_image3'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card3', 'imageName3')"})
        self.fields['location_image4'].widget.attrs.update({'class':'form-control storeImage', 'onchange': "imageUploaded(this, 'card4', 'imageName4')"})

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