from .forms import StoreForm
from core.models import User
from .models import Store
from apps.catalogue.models import ProductClass, Product

from django.shortcuts import get_object_or_404
from django.conf import settings


from store.forms import CommentForm
from core.mixins import BaseContextMixin

class settingsMixin(BaseContextMixin):
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
    


class PageTitleMixin(BaseContextMixin):
    """
    Passes page_title and active_tab into context, which makes it quite useful
    for the accounts views.

    Dynamic page titles are possible by overriding get_page_title.
    """

    page_title = None
    active_tab = None

    # Use a method that can be overridden and customised
    def get_page_title(self):
        return self.page_title

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.setdefault("page_title", self.get_page_title())
        ctx.setdefault("active_tab", self.active_tab)
        return ctx


class StoreMixin:
    """
        Common context data for the store
    """
    model = Product
    template_name='store/store.html'
    paginate_by= settings.STORE_PRODUCTS_PER_PAGE
    context_object_name ='products'
   
    form_class = CommentForm

    def get_store(self, **kwargs):
        return get_object_or_404(Store, **kwargs)
    
   
    def get_queryset(self):
        queryset = self.store.record.products.browsable().base_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commentForm'] = CommentForm(store=self.store, user=self.request.user)
        context['store'] = self.store
        context['user_productclass'] = ProductClass.objects.filter(products__seller=self.store.owner).distinct()
        return context