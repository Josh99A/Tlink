from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group

import datetime

from oscar.apps.customer.abstract_models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [("M","Male"), ("F", "Female")]
    LOCATION_CHOICES = [("BW", "Bweyale"), ("KY", 'Kyradongo')]
    phone_number = models.CharField(max_length=13)
    whatsApp = models.CharField(max_length=13, blank=True, null=True)
    date_of_birth = models.DateField(default=datetime.date(2024,1,1))
    location = models.CharField(max_length=2, choices=LOCATION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    has_accepted_terms_and_conditions = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profiles', default='blank-profile.png')

    @property
    def has_store(self):
        return hasattr(self, 'shop')



