from django.forms import ModelForm
from .models import Store, Comment

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['score'].widget.attrs.update({'class':'form-control d-none'})
        self.fields['message'].widget.attrs.update({'class':'form-control', 'cols':40, 'rows': 5, 'placeholder':'Enter your comment'})