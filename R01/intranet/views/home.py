from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from  ..models import Topic, Reply


class Home(View):

    template_name = 'intra/home.html'

    def get(self, request):
        topics = Topic.objects.all()
        context = {'topics': topics}
        print("=-=======================")
        print(dir(topics))
        print("=========================")
        return render(request, self.template_name, context)
