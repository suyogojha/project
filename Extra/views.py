from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Extra.models import *
from userprofile.decorators import *
from home.models import *

# Create your views here.



@login_required(login_url='userprofile:loginPage')
@admin_only
def certificates(request):
    data = mycertificatespic.objects.all()
    context = {"data": data}    
    return render(request, "certificates.html", context)
 
 
@login_required(login_url='userprofile:loginPage')
@admin_only
def projectcode(request):
    data = projectcodes.objects.all()
    context = {"data": data}   
    return render(request, "projectcode.html", context)


def videosproject(request):
    data = videosmyproject.objects.all()
    context = {"data": data}   
    return render(request, "videosproject.html", context)
 
 
@login_required(login_url='userprofile:loginPage')
@admin_only
def APIss(request):
    data = APILINKANDNAME.objects.all()
    context = {"data": data}  
    return render(request, "APIss.html", context)
 


def Team(request):
    data = myteamimg.objects.all()
    context = {"data": data}   
    return render(request, "Team.html", context)
 
 
 
 
@login_required(login_url='userprofile:loginPage')
@admin_only
def projectcode(request):
    data = projectcodes.objects.all()
    context = {"data": data}   
    return render(request, "projectcode.html", context)
 





def projectcodedetails(request,slug):
    newcode = projectcodes.objects.get(new_slug=slug)
    context = {
        "newcode": newcode,
        }
    return render(request, "projectcodedetails.html", context)









