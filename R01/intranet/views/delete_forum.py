from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from ..models import Topic


class Delete_forum(View):

    def get(self, redirect, forum_id):
        mycom = Topic.objects.get(id = forum_id)
        mycom.delete()
        return HttpResponseRedirect('/home/')
