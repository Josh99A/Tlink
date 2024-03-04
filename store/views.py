from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import TemplateView, View, DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from django.utils import timezone



from .forms import StoreForm, CommentForm, PasswordChangeForm
from core.models import User
from .models import Store, Product, StoreRecord
from .mixins import settingsMixin, PageTitleMixin
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


class StoreView(DetailView):
    model=Store
    template_name='store/store.html'
    view_signal = store_viewed

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.object == request.user.shop:
            self.send_signal(store=self.object, request=request, datetime=timezone.now())
        return super().get(request, *args, **kwargs)
    

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['commentForm'] = CommentForm(store=self.object, user=self.request.user)
        store_record_exists = StoreRecord.objects.filter(store=self.object).exists()

        if store_record_exists:
            context['products'] = context['store'].record.products.all()
        return context
    
    
    def send_signal(self, request, store, datetime):
        self.view_signal.send(
            sender=self,
            store=store,
            user= request.user,
            datetime=datetime
        )


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
        print(context)
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


