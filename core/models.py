from django.db import models

from oscar.apps.customer.abstract_models import AbstractUser

from subscription.models import Subscription


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=13)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,  null=True, blank=True)

