from unicodedata import category
from oscar.apps.analytics.abstract_models import AbstractProductRecord as OscarAbstractProductRecord, AbstractUserProductView as OscarUserProductView
from oscar.apps.analytics.abstract_models import AbstractUserRecord as OscarAbstractUserRecord, AbstractUserSearch as OscarAbstractUserSearch

from apps.catalogue.models import Category
from store.models import Store
from django.db import models

class ProductRecord(OscarAbstractProductRecord):
    category =  models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    store =  models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)


class UserRecord(OscarAbstractUserRecord):
    pass
    


class UserProductView(OscarUserProductView):
    pass


class UserSearch(OscarAbstractUserSearch):
    pass


from oscar.apps.analytics.models import * 
