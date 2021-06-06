from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from ..models import Topic, Comment
from ..forms import CommentForm

class Delete_comment(View):

    def get(self, request, com_id, current_id):
        mycom = Comment.objects.get(id = com_id)
        mycom.delete()
        return redirect('intranet:forum_detail', current_id)
