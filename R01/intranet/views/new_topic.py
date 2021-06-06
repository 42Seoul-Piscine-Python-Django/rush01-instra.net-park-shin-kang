from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from  ..models import Topic, Reply

class New_topic(View):

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

            user = User.objects.first()

            topic = Topic.objects.create(
                subject=subject,
                message=message,
                writter=user
            )

            post = Reply.objects.create(
                message=message,
                created_by=user

            )

            return redirect('intranet:home')



