from django.views import View
from  ..models import Topic, Profile
from ..forms import ProfileForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.http import HttpResponseRedirect, HttpResponse

class ProfileView(ListView):
    template_name = 'intra/profile.html'
    form_class=ProfileForm
    context_object_name='object_list'
    queryset = Profile.objects.all()

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context


    def post(self, request, forum_id):

        self.object_list = self.get_queryset()
        context = self.get_context_data()


        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                f = form.save(commit=False)
                f.user = request.user
                f.save()
                u = request.user
                u.email = form.cleaned_data['email']
                u.save()

            except Exception as e:
                print("e",e)

        print("3")
        
        forums = Topic.objects.filter(id=forum_id)
        profile = Profile.objects.filter(user=forums[0].writter)
        profile = profile[0]
        context['user_profile'] = profile

        context['form'] = ProfileForm()
        return self.render_to_response(context)

    def get(self, request, forum_id):
        self.object_list = self.get_queryset()
        try:
            forums = Topic.objects.filter(id=forum_id)
            context = {}
            try:
                profile = Profile.objects.filter(user=forums[0].writter)
                profile = profile[0]
            except Exception as e:
                profile = Profile(user=forums[0].writter)
            if not profile:
                profile = Profile(user=forums[0].writter)
            context['user_profile'] = profile

            if profile.user == request.user:
                context['form'] = ProfileForm()
        except Exception as e:
            print(e)
        
        return render(request, self.template_name, context)
