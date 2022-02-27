from django.urls import path
from databaseproject.views import *

app_name = "databaseproject"

urlpatterns = [
    path("databaseproject/", databaseproject, name="databaseproject"),
    
    path("studentdashboard/", studentdashboard, name="studentdashboard"),
    path("facultydashboard/", facultydashboard, name="facultydashboard"),
    
    path("modules/", modules, name="modules"),
    
    path("assignment/", assignment, name="assignment"),
    path("assignmentreceived/", assignmentreceived, name="assignmentreceived"),
    path("studentcomment/", studentcomment, name="studentcomment"),
    
    
    path("myassignment/", myassignment, name="myassignment"),
    path("assignmentfeedback/", assignmentfeedback, name="assignmentfeedback"),
    path("uploadassignment/", uploadassignment, name="uploadassignment"),
]




