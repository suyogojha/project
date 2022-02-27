from django.urls import path
from home.views import *


#APIS
from rest_framework.urlpatterns import format_suffix_patterns
from home import views



app_name = "home"

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("Extra/", Extra, name="Extra"),
    path("portfolio/", portfolio, name="portfolio"),
    path("contact_us/", contact_us, name="contact_us"),
    path("blog/", blog, name="blog"),
    path("blog_post/<slug>", blog_post, name="blog_post"),    
    
    
    
    #APIS
    
    path('api/', views.skillsList.as_view(), name="skillsList"),
    path('contactusAPI/', views.contactusAPI.as_view(), name="contactusAPI"),
    path('myblogAPI/', views.myblogAPI.as_view(), name="myblogAPI"),
    path('myportfilioAPI/', views.myportfilioAPI.as_view(), name="myportfilioAPI"),
    path('mycertificatespicAPI/', views.mycertificatespicAPI.as_view(), name="mycertificatespicAPI"),
    path('projectcodesAPI/', views.projectcodesAPI.as_view(), name="projectcodesAPI"),
    path('videosmyprojectAPI/', views.videosmyprojectAPI.as_view(), name="videosmyprojectAPI"),
    path('myteamimgAPI/', views.myteamimgAPI.as_view(), name="myteamimgAPI"),

]



