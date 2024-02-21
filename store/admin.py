from django.contrib import admin
from .models import Store, Comment, StoreRecord


admin.site.register(Store)
admin.site.register(StoreRecord)
admin.site.register(Comment)
