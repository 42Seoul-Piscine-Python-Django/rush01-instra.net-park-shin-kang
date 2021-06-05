from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 게시판 화면.
class Topic(models.Model):
    objects = models.Manager()
    message = models.TextField(max_length=5000,null=True)
    subject = models.CharField(max_length=255)
    last_updated =  models.DateField(auto_now_add=True, null=True)
    writter = models.ForeignKey(User, related_name='topics',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subject


# ForeignKey : 외래키.
# auto_now_add : 시간 기록.

# 댓글.
class Reply(models.Model):
    objects = models.Manager()
    message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by= models.ForeignKey(User, null=True, related_name='posts',on_delete=models.CASCADE)
    updated_at = models.DateField(null = True)
    updated_by=  models.ForeignKey(User,null=True,related_name='+',on_delete=models.CASCADE)

    def __str__(self):
        return self.message
