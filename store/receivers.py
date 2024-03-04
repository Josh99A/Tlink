from django.dispatch import receiver
from .signals import store_viewed

from apps.analytics.receivers import _update_counter
from store.models import UserStoreRecord

@receiver(store_viewed)
def user_store_record(sender, **kwargs):
    """
        Create or update a user store record when a store is viewed
    """
    _update_counter(UserStoreRecord, 'no_of_views', {'store': kwargs['store'], 'user': kwargs['user']})

    UserStoreRecord.objects.update(last_viewed=kwargs['datetime'])
