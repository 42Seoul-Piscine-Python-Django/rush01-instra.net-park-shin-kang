from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from ..models import Topic, Comment
from ..forms import CommentForm


class forum_Detail(View):
    """
    게시글 세부내용 출력
    """
    template_name = 'intra/forum_Detail.html'

    def get(self, request, forum_id):
        forum = get_object_or_404(Topic, pk=forum_id)
        mycom_form = CommentForm()
        current = Topic.objects.get(id = forum_id)
        context = {
            'forum' : forum,
            'comment_form':mycom_form,
            'current':current,
            }
        return render(request, self.template_name, context)


