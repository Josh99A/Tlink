from django.contrib import admin

from .models import User, StaticImage

admin.site.register(User)
admin.site.register(StaticImage)