from oscar.apps.analytics.admin import *
from oscar.apps.analytics.admin import ProductRecordAdmin as OscarProductRecordAdmin

from .models import ProductRecord
from django.contrib import admin

from oscar.core.loading import get_model

class ProductRecordAdmin(OscarProductRecordAdmin):
    list_display = ("product", "category", "store", "num_views", "num_basket_additions", "num_purchases") 

admin.site.unregister(ProductRecord)
admin.site.register(ProductRecord, ProductRecordAdmin)
