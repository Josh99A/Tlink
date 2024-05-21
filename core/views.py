from typing import Any
from django.db.models.base import Model as Model
from django.db.models import Q
from django.conf import settings
from django.views.generic import ListView,  TemplateView
from apps.catalogue.models import Product
from django.core.paginator import Paginator

from store.models import Store
from .models import User
from .mixins import BaseContextMixin

from apps.catalogue.models import Category


def get_category_products(category):
    category_products = []
    products = Product.objects.all()

    for product in products:
        product_cat = product.get_categories()[0]
        if product_cat.get_root() == category:
            category_products.append(product)

    return category_products



class indexList(BaseContextMixin, ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'
    paginate_by = settings.STORE_PRODUCTS_PER_PAGE

    def get_queryset(self):
        queryset = Product.objects.all().browsable().base_queryset()  
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        categories = Category.objects.all()
        root_categories = []
       
        for category in categories:
            if category.is_root():
                root_categories.append(category)
        
        stores = Store.objects.all()

        context['categories'] = root_categories
        context['stores'] = stores
        print(context)
        return context

class Subscribe(TemplateView):
    template_name = 'core/pricing.html'


class ProductStoreSearch(BaseContextMixin, ListView):
    model = Product
    template_name = 'core/results.html'
    context_object_name = 'products'
    paginate_by = settings.STORE_PRODUCTS_PER_PAGE
    tab = 'products'

    def get_queryset(self):
        # Product search
        self.q = self.request.GET.get('q', '').strip()
        queryset = Product.objects.filter(Q(title__icontains=self.q)).browsable().base_queryset()
        return queryset
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Store search
        stores = Store.objects.filter(Q(name__icontains=self.q))
        store_paginator = Paginator(stores,settings.STORE_PRODUCTS_PER_PAGE)
        page_number = self.request.GET.get("store_page")
        store_page_obj = store_paginator.get_page(page_number)
        context['store_paginator'] = store_paginator
        context['store_page_obj'] = store_page_obj
        context['stores'] = stores
        context['q'] = self.q
        context['tab'] = self.set_tab()
        print(context)
        return context
    
    def set_tab(self):
        urlTab = self.request.GET.get('tab')

        print('requet.GEt objects ', self.request.GET)
        if urlTab == 'store':
            return 'store'
        return self.tab
        
            
   




