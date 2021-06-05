from django.urls import path
from . import views

app_name = "intranet"

urlpatterns = [
    path('', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('register', views.Register.as_view(), name="register"),
    path('intranet', views.Homepage.as_view(), name="homepage"),
]
