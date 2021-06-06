from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from  ..models import Topic
from django.core.paginator import Paginator

class Home(View):
    """
    게시글 목록출력
    """
    template_name = 'intra/home.html'

    def get(self, request):
        page = request.GET.get('page', '1')
        topics = Topic.objects.all()
        paginator = Paginator(topics, 10)
        page_obj = paginator.get_page(page)
        context = {'topics': page_obj}
        return render(request, self.template_name, context)
