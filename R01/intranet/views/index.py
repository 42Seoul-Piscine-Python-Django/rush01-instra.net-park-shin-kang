from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

#['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

class Index(View):

    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
