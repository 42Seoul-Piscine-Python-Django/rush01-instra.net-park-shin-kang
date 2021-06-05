from django.urls import path
from . import views

from intranet import views

app_name = "intranet"

urlpatterns = [
    path('home/', views.Home.as_view(), name="home"),
    path('', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('home/new/',views.New_topic.as_view(),name='new_topic'),#게시글 작성 페이지 url 추가
]
