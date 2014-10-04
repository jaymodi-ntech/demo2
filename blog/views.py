from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import *
from django.views.generic import View
from blog.models import *

class Loginview(View):
    template1 = "login.html"
    template2 = "profile.html"
    def get(self, request):
        return render(request, self.template1)

    def post(self, request):


            print request.POST
            print "jay modi was here 1"
            username = request.POST.get('username')
            password = request.POST.get('password')

            if blog_user.objects.filter(username=username, password = password):
                context = blog_user.objects.filter(username= username)
                context_data = {'context_data': context}
                data = blog_user.objects.get(username=request.POST['username'])
                request.session["username"] = data.username
                session_data = request.session["username"]
                context_data.update({'session': session_data})

                print session_data
                print "jay modi was here twice"

                print context_data
                print "jay modi was here three times"
                return render(request, self.template2, context_data)
            else:
                return render(request, self.template1)
        # if "username" in request.session:
        # else:
        #     return render(request, self.template1)

class Logout_view(View):
    template1 = "login.html"

    def get(self, request):

        if "username" in request.session:
            print "You have successfully logged out"
            del request.session["username"]
            return render(request,self.template1)
        else:
            return render(request, self.template1)


class Signup_view(View):

    template1 = 'signup.html'
    template2 = 'welcome.html'

    def get(self, request):
        return render(request, self.template1)

    def post(self, request):
        print request.POST
        name = request.POST.get('name')
        address = request.POST.get('address','')
        age = request.POST['age']
        gender = request.POST.get('gen')
        contact = request.POST.get('contact')
        city = request.POST.get('city')
        username = request.POST.get('username')
        password = request.POST.get('password')

        u  = blog_user(name = name,gender=gender, address = address, age = age, contact = contact, city = city, username = username, password = password)
        u.save()

        return render(request, self.template2)