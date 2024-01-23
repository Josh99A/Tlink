from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from core.models import User
from datetime import datetime


from apps.catalogue.models import Product

class Store(models.Model):
    location_choices =[('BW', 'Bweyale'), ('KY', 'Kyradongo')]
    name = models.CharField(max_length=15)
    owner = models.OneToOneField(User, related_name="shop", on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=location_choices)
    staff = models.ManyToManyField(User, related_name='stores')
    products = models.ManyToManyField(Product, related_name='store', blank=True)
    slug = models.SlugField()
    date_created = models.DateField('Date created', auto_now_add=True)
    date_modified = models.DateTimeField('Date modified', auto_now=True)
    primary_image = models.ImageField(upload_to='store')
    location_image1 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image2 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image3 = models.ImageField(upload_to='location', default='image_not_found.jpg')
    location_image4 = models.ImageField(upload_to='location', default='image_not_found.jpg')

    def __str__(self):
        return self.name
    
    def get_slug(self):
        return slugify(self.name)

class Comment(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    message = models.TextField('Body')
    
    date_created = models.DateField('Date created', auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comments')
    # Scores are between 0 and 5
    SCORE_CHOICES = tuple([(x, x) for x in range(0, 6)])
    score = models.SmallIntegerField( "Score", choices=SCORE_CHOICES)


    def __str__(self):
        return self.title
    
    
    def clean(self):
        if  self.store.owner == self.user:
            raise ValidationError("You cannot comment on your own store")
        if not self.user.id:
            raise ValidationError("Only signed-in users can comment on stores")
        previous_comments = self.store.commnets.filter(user=self.user)
        if len(previous_comments) > 0:
                raise ValidationError("You can only comment once on a store")