from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from userprofile.decorators import *
from databaseproject.models import *


# Create your views here.
@login_required(login_url='userprofile:loginPage')
@admin_only
def databaseproject(request):
    return render(request, "databaseproject.html")
 

@login_required(login_url='userprofile:loginPage')
def studentdashboard(request):
    context = {}
    return render(request, "studentdashboard.html", context)


@login_required(login_url='userprofile:loginPage')
def facultydashboard(request):
    context = {}
    return render(request, "facultydashboard.html", context)

@login_required(login_url='userprofile:loginPage')
def modules(request):
    data = modulesdetails.objects.all()
    context = {
        "data": data,
        }  
    return render(request, "modules.html", context)



@login_required(login_url='userprofile:loginPage')
def assignment(request):
    if request.method =='POST':
        Postassignments = postassignments()
        modulename = request.POST.get('modulename')
        modulecode = request.POST.get('modulecode')
        releasedate = request.POST.get('releasedate')
        duedate = request.POST.get('duedate')
        question = request.POST.get('question')
        file = request.FILES.get('file')
        message = request.POST.get('message')
    
        Postassignments.modulename = modulename
        Postassignments.modulecode = modulecode
        Postassignments.releasedate = releasedate
        Postassignments.duedate = duedate
        Postassignments.question = question
        Postassignments.file = file
        Postassignments.message = message
        Postassignments.save()

    return render(request, "assignment.html")




@login_required(login_url='userprofile:loginPage')
def assignmentreceived(request):
    if request.method == 'POST':
        Teacherfeedback = teacherfeedback()
        message = request.POST.get('message')
        To = request.POST.get('To')
        feedback = request.POST.get('feedback')
        Teacherfeedback.message = message
        Teacherfeedback.To = To
        Teacherfeedback.feedback = feedback
        Teacherfeedback.save()

    data = uploadassignments.objects.all()
    context = {
        "data": data,
        } 
    return render(request, "assignmentreceived.html", context)





@login_required(login_url='userprofile:loginPage')
def myassignment(request):
    data = postassignments.objects.all()

    context = {
        "data": data,

        }  
    return render(request, "myassignment.html", context)



@login_required(login_url='userprofile:loginPage')
def uploadassignment(request):
    if request.method == 'POST':
        Uploadassignments = uploadassignments()
        file = request.FILES.get('file')
        subject = request.POST.get('subject')
        Name = request.POST.get('Name')
        message = request.POST.get('message')
        
        Uploadassignments.file = file
        Uploadassignments.subject = subject
        Uploadassignments.Name = Name
        Uploadassignments.message = message
        Uploadassignments.save() 
    context = {
    }
    return render(request, "uploadassignment.html", context)



@login_required(login_url='userprofile:loginPage')
def assignmentfeedback(request):
    data = teacherfeedback.objects.all()
    if request.method == 'POST':
        Studentmsg = studentmsg()
        Name = request.POST.get('Name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Studentmsg.Name = Name
        Studentmsg.subject = subject
        Studentmsg.message = message
        Studentmsg.save()          
    
    context = {
       "data": data,

        }  
    return render(request, "assignmentfeedback.html", context)





@login_required(login_url='userprofile:loginPage')
def studentcomment(request):   
    data = studentmsg.objects.all()
 
    context = {
       "data": data,
        }  
    return render(request, "studentcomment.html", context)



