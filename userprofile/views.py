from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from userprofile.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from userprofile.decorators import *
from django.contrib.auth.models import Group
# Create your views here.


#login for certificate

@unauthenticated_user
def loginPage(request):	
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('home:Extra')
        else:
                messages.info(request, 'Username OR password is incorrect')
    
    context = {} 
    return render(request, "login.html", context)
 
    

@unauthenticated_user
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account was created for ' + username)
            return redirect('userprofile:loginPage')
                
    context = {'form': form}
    return render(request, "signup.html", context)
 
              
def logoutUser(request):
	logout(request)
	return redirect('userprofile:loginPage')



def Theuser(request):
    context = {}
    return render(request, "Theuser.html", context)








 