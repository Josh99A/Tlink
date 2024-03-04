from unicodedata import category
from oscar.apps.catalogue.abstract_models import AbstractProduct as BaseProduct, AbstractProductClass as BaseAbstractProductClass
from oscar.apps.catalogue.abstract_models import AbstractCategory as OscarAbstractCategory


from django.db import models
from django.urls import reverse

from core.models import User


class Category(OscarAbstractCategory):
    # def get_absolute_url(self):
    #     return reverse(f'core:{self.name}'.lower(), kwargs={'slug': self.slug, 'str': self.name.lower()})
    pass

class ProductClass(BaseAbstractProductClass):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    
class Product(BaseProduct):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)




from oscar.apps.catalogue.models import * 
