from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from  ..models import Topic


class forum_Detail(View):
    """
    pybo 내용 출력
    """
    template_name = 'intra/forum_Detail.html'

    def get(self, request, forum_id):
        forums = get_object_or_404(Topic, pk=forum_id)
        print("forums ==========", dir(forums))
        context = {'forums' : forums}
        return render(request, self.template_name, context)
