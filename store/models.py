from django.db import models
from core.models import User

from apps.catalogue.models import Product

class Store(models.Model):
    location_choices =[('BW', 'Bweyale'), ('KY', 'Kyradongo')]
    name = models.CharField(max_length=15)
    location = models.CharField(max_length=20, choices=location_choices)
    staff = models.ManyToManyField(User, related_name='stores')
    products = models.ManyToManyField(Product, related_name='store')
    primary_image = models.ImageField(upload_to='store')
    location_image1 = models.ImageField(upload_to='location')
    location_image2 = models.ImageField(upload_to='location', blank=True, null=True)
    location_image3 = models.ImageField(upload_to='location', blank=True, null=True)
    location_image4 = models.ImageField(upload_to='location', blank=True, null=True)

    def __str__(self):
        return self.name