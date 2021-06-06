from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from ..forms import NewUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages #import messages


class Register(View):

    template_name = 'register.html'

    def get(self, request):
        form = NewUserForm
        return render (request, self.template_name, context={"register_form":form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("intranet:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return render (request, self.template_name, context={"register_form":form})

