__author__ = 'mj'
from django.shortcuts import *
from auth_app.forms import UserForm, UserProfileForm
from django.contrib.auth.models import *
from django.views.generic import View

# class register_view(View):
#     template1= "some.html"
#     template2 = "some.html"
#     registered = False
#
#     def get(self, request):
#         return render(request,self.template1)
#
#     def post(self, request):
#
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#                 profile.save()
#                 registered = True
#             else:
#                 print user_form.errors, profile_form.errors
#
#         else:
#             user_form = UserForm()
#             profile_form = UserProfileForm()
#
#             return render_to_response(
#                 'rango/register.html',
#                 {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
#                 context)
#
#         return render(request, self.template2)

def register(request):

    context = RequestContext(request)


    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'auth_app/auth_signup.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)
