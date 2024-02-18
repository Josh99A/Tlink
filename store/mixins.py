from .forms import StoreForm
from core.models import User
from .models import Store

class settingsMixin(object):
    def get(self, request, *args, **kwargs):
        # Get the user shop 
        try: 
            user_shop = Store.objects.get(owner=request.user)
        except (User.shop.RelatedObjectDoesNotExist, Store.DoesNotExist):
            # create if it does not exist
            user_shop = Store(owner=request.user, primary_image=request.user.profile_image)
            user_shop.save() 


        self.form = StoreForm(instance=user_shop)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('storeForm', self.form)
        return context

