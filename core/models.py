from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

from subscription.models import Subscription


class User(AbstractUser):
    GENDER_CHOICES = [("M","Male"), ("F", "Female")]
    LOCATION_CHOICES = [("BW", "Bweyale"), ("KY", 'Kyradongo')]
    username = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    loation = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile = models.ImageField(upload_to='profiles', default='blank-profile.png')
    referral_code = models.TextField(max_length=6, unique=True)
    referrals = models.ManyToManyField('self')
    referral_url = models.URLField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,  null=True, blank=True)