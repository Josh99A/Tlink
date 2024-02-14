from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import User
from django.contrib.auth.models import Group


@receiver(post_save, sender=User)
def add_to_basic(sender, instance, **kwargs):
    base_group = Group.objects.filter(name='Basic').first()
    if base_group and not instance.groups.contains(base_group):
        instance.groups.add(base_group)
   