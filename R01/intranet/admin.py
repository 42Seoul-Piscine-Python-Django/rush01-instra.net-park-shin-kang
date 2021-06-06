from django.contrib import admin
from  .models import Topic, Reply

# Register your models here.

admin.site.register(Reply)
admin.site.register(Topic)

