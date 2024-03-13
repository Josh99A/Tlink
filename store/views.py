import re
from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView, View, DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from django.utils import timezone


from core.mixins import BaseContextMixin



from .forms import StoreForm, CommentForm, PasswordChangeForm
from core.models import User
from .models import Store, Product, StoreRecord
from .mixins import settingsMixin, PageTitleMixin, StoreMixin
from .signals import store_viewed


from apps.dashboard.catalogue.views import ProductListView
from apps.customer.views import ProfileUpdateView, ProfileDeleteView, ChangePasswordView
from apps.customer.views import ProfileView
from apps.catalogue.models import Category



class SettingsView(settingsMixin, ProfileView):
    template_name = 'store/profile.html'
    active_tab = 'store_settings'
    page_title = 'Profile'


class ProfileUpdateView(settingsMixin, ProfileUpdateView):
    template_name = 'store/profile_form.html'
    active_tab = 'profile'
    success_url = reverse_lazy('store:settings')

class ProfileDeleteView(settingsMixin, ProfileDeleteView):
    template_name = 'store/profile_delete.html'
    active_tab = 'profile'
    success_url = reverse_lazy('core:index')


class ChangePasswordView(settingsMixin, ChangePasswordView):
    form_class = PasswordChangeForm
    template_name = 'store/change_password.html'
    success_url = reverse_lazy('store:settings')


class StoreCreationView(PageTitleMixin, SingleObjectMixin,FormView ):
    """
     Get the existing user store and create a form for updating it.

    """
    template_name = 'store/profile.html'
    form_class = StoreForm
    model = User
    active_tab = 'store_settings'

    def post(self, request, *args, **kwargs):
        storeForm = self.form_class(request.POST, request.FILES, instance=request.user.shop)
        self.object = self.get_object()
        if storeForm.is_valid():
           store = storeForm.save(commit=False)
           store.slug = store.get_slug()
           store.prompted = True
           store.save()
           storeForm.save_m2m()

           # Create a store record if it does not exist
           store_record_exists = StoreRecord.objects.filter(store=store).exists()

           if not store_record_exists:
                store_record =  StoreRecord.objects.create(store=store)
                store_record.staff.add(request.user)

           message = "Your store has successfully been created. Enjoy"
           messages.success(request, message)
           return redirect(reverse('store:settings'))
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

        request.user.profile_image = new_image
        request.user.save()
        # Update Store image
        if hasattr(request.user, 'shop'):
            request.user.shop.primary_image = request.user.profile_image
            request.user.shop.save()
        new_image_url = request.user.profile_image.url

        return JsonResponse({'new_image': new_image_url })
    
class FollowView(LoginRequiredMixin, BaseContextMixin, StoreMixin, DetailView):
    model =Store
    template_name = 'store/store.html'
    redirect_field_name = 'next'

    def get(self, request , *args, **kwargs):
        store = self.get_object()

        if request.user in store.record.store_followers.all():
            store.record.store_followers.remove(request.user)
        else:
            store.record.store_followers.add(request.user)

        return super().get(request ,*args, **kwargs)

    def get_redirect_field_name(self) -> str:
        print(super().get_redirect_field_name())
        return super().get_redirect_field_name()
    
    def post(self, request, *args, **kwargs):
        store_id = int(request.POST['store_id'])
        store = Store.objects.filter(id=store_id).first()

        if request.user in store.record.store_followers.all():
            store.record.store_followers.remove(request.user)
            is_follower = False
        else:
            store.record.store_followers.add(request.user)
            is_follower = True

        followers_count = store.record.store_followers.all().count()
        

        return JsonResponse({'followers_count': followers_count, 'is_follower': is_follower}) 



class StoreView(BaseContextMixin, StoreMixin, DetailView):
    model=Store
    template_name='store/store.html'
    view_signal = store_viewed

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if request.user.is_authenticated:
            if not self.object == request.user.shop:
                self.send_signal(store=self.object, user=request.user , datetime=timezone.now())
                
        return super().get(request, *args, **kwargs)
    

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['commentForm'] = CommentForm(store=self.object, user=self.request.user)
        store_record_exists = StoreRecord.objects.filter(store=self.object).exists()
        if store_record_exists:
            context['products'] = context['store'].record.products.all()
        print(context)
        return context
    
    
    def send_signal(self, user, store, datetime):
        self.view_signal.send(
            sender=self,
            store=store,
            user= user,
            datetime=datetime
        )


class StoreCommentView(BaseContextMixin, StoreMixin, SingleObjectMixin, View):
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


class DashBoardView(ProductListView):
    model = Product
    template_name = 'store/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        """
            Set a limit to the number of products based on the subscription package:
            Basic - 15 products
            Premium - 30 products
            Enterprise - Unlimited products

        """
        is_enterprise = False
        if request.user.groups.all().first().name == 'Enterprise':
            is_enterprise = True
        print('Is Enterprise', is_enterprise)
        print('Group', request.user.groups.all().first().name)

        if request.user.is_authenticated and not is_enterprise  :
            user_product_count = request.user.shop.record.products.count()
            user_group = request.user.groups.all().first().name
            product_limit = settings.BASIC_PRODUCT_LIMIT
            if user_group == 'Premium':
                product_limit = settings.PREMIUM_PRODUCT_LIMIT
            print('Product limit: ', product_limit)

            if user_product_count >= product_limit:
                messages.error(request, 'Update to premium or enterprise to add more products')
                print('Redirecting now to dashboard')
                return redirect(reverse('store:dashboard', kwargs={'pk': request.user.pk}))
            
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['root_category'] = Category.objects.get(name=kwargs['category'])
        context['productclass_categories'] = context['root_category'].get_descendants().filter(productclass__isnull=False).distinct()
        return context


