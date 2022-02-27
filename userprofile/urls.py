from django.urls import path
from userprofile.views import *

app_name = "userprofile"

urlpatterns = [
    path("loginPage/", loginPage, name="loginPage"),
    path("signup/", signup, name="signup"),
    path("logout/", logoutUser, name="logout"),
    path("Theuser/", Theuser, name="Theuser"),
    

]
