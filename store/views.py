from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, View

class SettingsView(TemplateView):
    template_name = 'store/settings.html'


class ProfileImageView(View):
    def post(self, request, *args, **kwargs):
        upload_image = request.FILES.get('profile_image')

        profile_image_url = '/media/profiles/' + str(upload_image)


        return JsonResponse({'profile_image_url': profile_image_url})

class UpdateProfileImageView(View):
    def post(self, request, *args, **kwargs):
        print(request.POST)
        profile_image_url = request.POST.get('profile_image_url')

        if profile_image_url:
            request.user.profile = profile_image_url
            request.user.save()
        else:
            print('Not found')
            print(profile_image_url)
        return JsonResponse({'message': 'Profile image updated successfully'})



