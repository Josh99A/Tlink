from django.db import models


class Subscription(models.Model):
    type = models.CharField(max_length=20)
    price = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return self.type
