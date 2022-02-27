from django.shortcuts import redirect, render,reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from Extra.models import *



#APIS
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.


# for home
def home(request):
    mimg = myprofilepic.objects.all()
    context = {
        "mimg": mimg,      
     
        }
    return render(request, "index.html", context)

# redirect to about us
def about(request):
    data = myskillsabout.objects.all()
    myimg = myprofilepic.objects.all()

    context = {
        "data": data, 
        "myimg": myimg,      
     
        }
    return render(request, "about.html",  context)

def Extra(request):
    return render(request, "Extra.html")


# redirect to portfolio
def portfolio(request):
    data = myportfilio.objects.all()
    context = {"data": data}
    return render(request, "portfolio.html", context)


def contact_us(request):
    if request.method =='POST':
        contact = contactus()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
    return render(request, 'contact_us.html')


def blog(request):
    data = myblog.objects.all()
    context = {"data": data}
    return render(request, "blog.html", context)


def blog_post(request,slug):
    newblog = myblog.objects.get(new_slug=slug)
    context = {
        "newblog": newblog,
        }
    return render(request, "blog_post.html", context)






# APIS



class skillsList(APIView):
    
    def get(self, request):
        skill1 = myskillsabout.objects.all()
        serializer = skillsserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    

class contactusAPI(APIView):
    
    def get(self, request):
        skill1 = contactus.objects.all()
        serializer = contactusserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
    
    

class myblogAPI(APIView):
    
    def get(self, request):
        skill1 = myblog.objects.all()
        serializer = myblogserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    


class myportfilioAPI(APIView):
    
    def get(self, request):
        skill1 = myportfilio.objects.all()
        serializer = myportfilioserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
    
class mycertificatespicAPI(APIView):
    
    def get(self, request):
        skill1 = mycertificatespic.objects.all()
        serializer = mycertificatespicserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
class projectcodesAPI(APIView):
    
    def get(self, request):
        skill1 = projectcodes.objects.all()
        serializer = projectcodesserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
           
class videosmyprojectAPI(APIView):
    
    def get(self, request):
        skill1 = videosmyproject.objects.all()
        serializer = videosmyprojectserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
    
class myteamimgAPI(APIView):
    
    def get(self, request):
        skill1 = myteamimg.objects.all()
        serializer = myteamimgserializers(skill1, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass
                   
    

    
    
    