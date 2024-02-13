from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView,  View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from apps.catalogue.models import Product
from .forms import UserCreationForm
from django.views.generic.edit import CreateView
from core.models import User

from apps.catalogue.models import Category


def get_category_products(category):
    category_products = []
    products = Product.objects.all()

    for product in products:
        product_cat = product.get_categories()[0]
        if product_cat.get_root() == category:
            category_products.append(product)

    return category_products



class indexList(ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        categories = Category.objects.all()
        root_categories = []

        for category in categories:
            if category.is_root():
                root_categories.append(category)
        
        

        context['categories'] = root_categories
        return context

class Subscribe(TemplateView):
    template_name = 'core/pricing.html'

class FashionCategory(DetailView):
    template_name = 'core/Fashion/Fashion.html'
    context_object_name = 'Fashion'

    def get_object(self) :
        self.category = Category.objects.get(name='Fashion')
        return self.category
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['category_products'] = get_category_products(self.category)
        print(context)
        return context
    




class UserStoreView(SingleObjectMixin, ListView):
    template_name= 'core/Store.html'
    context_object_name = 'Product_list'
    

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())

        return super().get(request, *args, **kwargs) 

   

    def get_context_data(self, **kwargs):
        user = self.object
        context = super().get_context_data(**kwargs)
        context['user'] = user
        context['product_list'] = context['object_list']
        print(context)
        return context

    def get_queryset(self):
        return self.object.product_set.all()
   



