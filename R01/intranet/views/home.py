from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from  ..models import Topic, Reply
from django.core.paginator import Paginator

class Home(View):
    """
    pybo 목록출력
    """
    template_name = 'intra/home.html'

    def get(self, request):
        topics = Topic.objects.all()
        paginator = Paginator()
        context = {'topics': topics}
        return render(request, self.template_name, context)
