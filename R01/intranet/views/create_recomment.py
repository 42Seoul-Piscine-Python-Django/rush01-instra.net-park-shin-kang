from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, logout, authenticate
from ..models import Topic, Comment
from ..forms import CommentForm, ReCommentForm


class Create_recomment(View):

    def get(self, request, current_id):
        return redirect('intranet:forum_detail', current_id)

    def post(self, request, current_id):
        filled_form = ReCommentForm(request.POST)
        if filled_form.is_valid():
            temp_form = filled_form.save(commit=False)
            temp_form.writter = self.request.user
            temp_form.save()
        return redirect('intranet:forum_detail', current_id)
