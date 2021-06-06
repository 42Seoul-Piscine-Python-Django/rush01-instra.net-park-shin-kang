from django.urls import path
from . import views

from intranet import views

app_name = "intranet"

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('home/', views.Home.as_view(), name="home"),
    path('home/new/',views.New_topic.as_view(),name='new_topic'), #게시글 작성 페이지 url 추가
    path('home/<int:forum_id>/',views.forum_Detail.as_view(),name='forum_detail'), #게시글 작성 페이지 url 추가
    path('create_comment/<int:current_id>/',views.Create_comment.as_view(),name='create_comment'), #게시글 작성 페이지 url 추가
]
