__author__ = 'mj'
from django.shortcuts import *
from auth_app.forms import UserForm, UserProfileForm
from django.contrib.auth.models import *
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from auth_app.models import UserProfile

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


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print user
        if user:
            if user.is_active:
                login(request, user)
                # data = User.objects.filter(username = username)
                # context_data = {'context_data': data}
                # return render(request, 'auth_app/welcome.html', context_data)
                return render_to_response('auth_app/welcome.html')
                # return HttpResponseRedirect('/auth_app/welcome.html')
            else:
                return HttpResponse("Your MJ account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:

        return render_to_response('auth_app/auth_login.html', context)

def logout_view(request):
    logout(request)
    return render_to_response('auth_app/logout.html')

