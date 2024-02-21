from django.db import models
from django.utils.text import slugify
from core.models import User
from datetime import datetime


from apps.catalogue.models import Product

class Store(models.Model):
    location_choices =[('BW', 'Bweyale'), ('KY', 'Kyradongo')]
    name = models.CharField(max_length=15)
    owner = models.OneToOneField(User, related_name="shop", on_delete=models.CASCADE)
    location = models.CharField(max_length=20, choices=location_choices)
    is_active = models.BooleanField(default=False)
    prompted = models.BooleanField(default=False)
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

class StoreRecord(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE ,  related_name='record')
    views = models.IntegerField(default=0)
    # Ratings are between 0 and 5
    RATING_CHOICES = tuple([(x, x) for x in range(0, 6)])
    rating = models.PositiveSmallIntegerField( "Rating", choices=RATING_CHOICES, default=0)
    products = models.ManyToManyField(Product, related_name='store', blank=True)
    staff = models.ManyToManyField(User, related_name='stores')
    followers = models.ManyToManyField(User)

    def __str__(self):
        return self.store.name


class Comment(models.Model):
    title = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    message = models.TextField('Body')
    
    date_created = models.DateField('Date created', auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='comments')
    # Scores are between 0 and 5
    SCORE_CHOICES = tuple([(x, x) for x in range(0, 6)])
    score = models.PositiveSmallIntegerField( "Score", choices=SCORE_CHOICES)


    def __str__(self):
        return self.title
    
