from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,  View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from apps.catalogue.models import Product
from .forms import UserCreationForm
from django.views.generic.edit import CreateView
from core.models import User

from oscar.apps.catalogue.models import Category



class indexList(ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)

        categories = Category.objects.all()
        root_categories = []

        for category in categories:
            if category.is_root():
                root_categories.append(category)


        context['categories'] = root_categories
        return context

class Subscribe(TemplateView):
    template_name = 'core/subscription_plans.html'

class FashionCategory(DetailView):
    template_name = 'core/Fashion/Fashion.html'
    context_object_name = 'Fashion'

    def get_object(self) :
        return Category.objects.get(name='Fashion')

class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'core/Forms/signup.html'

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
   



