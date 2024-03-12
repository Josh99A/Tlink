from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView,  View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from apps.catalogue.models import Product

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

   




