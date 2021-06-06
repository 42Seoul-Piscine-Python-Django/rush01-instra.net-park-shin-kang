from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from  ..models import Topic
from django.views.generic import ListView

class New_topic(ListView):
    """
    게시글 작성.
    """
    template_name = 'intra/new_topic.html'

    def get(self, request):
        topics = Topic.objects.all()
        context = {'topics': topics}
        return render(request, self.template_name, {'topics':topics})

    def post(self, request):
        topics = Topic.objects.all()
        if request.method =='POST':
            subject = request.POST['subject']
            message = request.POST['message']

            user = self.request.user
            print("=====================================")
            print("message = ", message)
            print("=====================================")
            topic = Topic.objects.create(
                subject=subject,
                message=message,
                writter=user
            )

            return redirect('intranet:home')



