from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, View, DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from .forms import StoreForm, CommentForm
from core.models import User
from .models import Store, Product

from apps.catalogue.models import Category

class SettingsView(DetailView):
    model= User
    template_name = 'store/settings.html'

    def get(self, request, *args, **kwargs):
        print("Started get request")
        # Get the user shop 
        try: 
            user_shop = Store.objects.get(owner=request.user)
        except (User.shop.RelatedObjectDoesNotExist, Store.DoesNotExist):
            # create if it does not exist
            user_shop = Store(owner=request.user, primary_image=request.user.profile)
            user_shop.save() 


        self.form = StoreForm(instance=user_shop)

        return super().get(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['storeForm'] = self.form
        return context

class StoreCreationView(SingleObjectMixin, FormView):
    template_name = 'store/settings.html'
    form_class = StoreForm
    model = User

    def post(self, request, *args, **kwargs):
        storeForm = self.form_class(request.POST, request.FILES, instance=request.user.shop)
        self.object = self.get_object()
        if storeForm.is_valid():
           store = storeForm.save(commit=False)
           store.staff.add(request.user)
           store.slug = store.get_slug()
           store.save()
           return redirect(reverse('store:settings', kwargs={'pk':self.object.pk}))
        else:
            context = self.get_context_data(storeForm=storeForm)
            return render(request, self.template_name, context)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for kw in kwargs:
            context[kw] = kwargs[kw]
        return context
        
    


    
class UploadProfileImageView(View):
    def post(self, request, *args, **kwargs):
        new_image = request.FILES.get('profile-image')

        request.user.profile = new_image
        request.user.save()
        # Update Store image
        if hasattr(request.user, 'shop'):
            request.user.shop.primary_image = request.user.profile
            request.user.shop.save()
        new_image_url = request.user.profile.url

        return JsonResponse({'new_image': new_image_url })



class StoreView(DetailView):
    model=Store
    template_name='store/store.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        print('Object', self.object)
        context['commentForm'] = CommentForm(store=self.object, user=self.request.user)
        context['products'] = context['store'].products.all()
        print(context)
        return context

class StoreCommentView(SingleObjectMixin, View):
    model=Store
    form_class = CommentForm
    template_name = 'store/store.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() 
        commentForm = self.form_class(data=request.POST, store=self.object, user=request.user)
       
 
        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.store = self.object
            comment.user = request.user
            comment.save()
            return redirect(reverse('store:store', kwargs={'pk':self.object.pk, 'slug':self.object.get_slug()}))
        else:
            context = self.get_context_data(commentForm=commentForm)
            return render(request, self.template_name, context)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        for kw in kwargs:
            context[kw] = kwargs[kw]
        return context


class DashBoardView(ListView):
    model = Product
    template_name = 'store/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)

        categories = Category.objects.all()
        root_categories = []

        for category in categories:
            if category.is_root():
                root_categories.append(category)
        
        

        context['categories'] = root_categories
        return context


class ProductCreation(TemplateView):
    template_name='store/dashboard/product_addition.html'


    def get(self, request, *args, **kwargs ):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['root_category'] = Category.objects.get(name=kwargs['category'])
        context['productclass_categories'] = context['root_category'].get_descendants().filter(productclass__isnull=False).distinct()
        return context