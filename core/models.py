from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

from oscar.apps.customer.abstract_models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [("M","Male"), ("F", "Female")]
    LOCATION_CHOICES = [("BW", "Bweyale"), ("KY", 'Kyradongo')]
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profile = models.ImageField(upload_to='profiles', default='blank-profile.png')




