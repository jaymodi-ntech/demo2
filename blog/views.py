from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import *
from django.views.generic import View
from blog.models import *

class Loginview(TemplateView):
    template_name = "login.html"

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