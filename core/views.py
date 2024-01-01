from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,  View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from apps.catalogue.models import Product
from .forms import UserCreationForm
from django.views.generic.edit import CreateView
from core.models import User



class indexList(ListView):
    model = Product
    template_name = 'core/index.html'
    context_object_name = 'products'

class Subscribe(TemplateView):
    template_name = 'core/subscription_plans.html'

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
   



