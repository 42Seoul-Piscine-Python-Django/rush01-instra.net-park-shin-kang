from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages #import messages
from django.contrib.auth import login, logout, authenticate


class Login(View):

    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('intranet:homepage')
        form = AuthenticationForm()
        return render(request=request, template_name="login.html", context={"login_form":form})


    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("intranet:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

