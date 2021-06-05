from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages #import messages
from django.contrib.auth import login, logout, authenticate


class Homepage(View):

    def get(self, request):
        return render(request, 'intranet.html')
