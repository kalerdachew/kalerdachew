from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Userregisterform

def register(request):
   if (request.method=='POST'):
     form=Userregisterform(request.POST)
     if form.is_valid():
       form.save()
       username=form.cleaned_data.get('username')
       messages.info(request, f'account created for {username}!')
       return redirect('blog-log')
   else:
    form=Userregisterform()
   return render(request,'users/register.html',{'form':form})