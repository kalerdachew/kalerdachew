from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages
from django.contrib.auth.decorators import login_required    #requiring the user to login first
from .forms import userregister,updateform,profileupdateform  #importing the userregister form created in forms.py
#from django.http import HttpResponse
from django.forms import ModelForm
from PIL import Image
def register(request):
 if(request.method=='POST'):
    form=userregister(request.POST)
    if form.is_valid():     # a user will be created if and only if the form is valid
     form.save()
     username=form.cleaned_data.get('username')
     messages.success(request,f'you have successfully created your account by {username} you can login now!!!!!')
     return redirect('login')
 else:
   form=userregister()
 return(render(request, 'register.html',{'form':form}))
 def login(request):
  return(render(request, "login.html"))

def logout(requset):
    return(render(request, "logout.html"))
@login_required()
def profile(request):
  if(request.method=='POST'):
    u_form=updateform(request.POST,instance=request.user)
    p_form=profileupdateform(request.POST,
    request.FILES,
    instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request,f'your account profile has been updated sucessfully')
       return redirect('user-profile')
  else:
    u_form=updateform(instance=request.user)
    p_form=profileupdateform(instance=request.user.profile)
  context={
    'u_form':u_form,
    'p_form':p_form
  }
  return render(request, "profile.html",context)
  
# Create your views here.

