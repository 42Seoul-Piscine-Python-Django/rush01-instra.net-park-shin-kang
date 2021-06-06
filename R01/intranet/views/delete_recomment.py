from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from ..models import Topic, Comment, ReComment
from ..forms import CommentForm, ReCommentForm

class Delete_recomment(View):

    def get(self, request, recom_id, current_id):
        mycom = ReComment.objects.get(id = recom_id)
        mycom.delete()
        return redirect('intranet:forum_detail', current_id)
