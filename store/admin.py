from django.contrib import admin
from .models import Store, Comment, StoreRecord, UserStoreRecord

class UserStoreRecordAdmin(admin.ModelAdmin):
    list_display = ('user' , 'store', 'no_of_views', 'date_viewed', 'last_viewed')

admin.site.register(Store)
admin.site.register(StoreRecord)
admin.site.register(Comment)
admin.site.register(UserStoreRecord, UserStoreRecordAdmin)
