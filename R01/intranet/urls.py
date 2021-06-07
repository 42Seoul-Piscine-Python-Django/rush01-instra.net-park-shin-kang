from django.urls import path
from . import views

from intranet import views

app_name = "intranet"

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('logout/', views.Logout.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('home/', views.Home.as_view(), name="home"),
    path('home/new/',views.New_topic.as_view(),name='new_topic'),
    path('home/<int:forum_id>/',views.forum_Detail.as_view(),name='forum_detail'),
    path('home/delete_forum/<int:forum_id>/', views.Delete_forum.as_view(),name='delete_forum'),
    path('create_comment/<int:current_id>/',views.Create_comment.as_view(),name='create_comment'),
    path('delete_comment/<int:com_id>/<int:current_id>', views.Delete_comment.as_view() , name="delete_comment"),
    path('create_recomment/<int:current_id>', views.Create_recomment.as_view() , name="create_recomment"),
    path('delete_recomment/<int:recom_id>/<int:current_id>', views.Delete_recomment.as_view() , name="delete_recomment"),
    path('profile/<int:forum_id>',views.ProfileView.as_view(),name='profile'),
]
