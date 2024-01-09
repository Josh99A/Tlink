from oscar.apps.catalogue.abstract_models import AbstractProduct as BaseProduct

from django.db import models

from core.models import User


class Product(BaseProduct):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


from oscar.apps.catalogue.models import * 
