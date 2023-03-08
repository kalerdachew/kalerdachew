from django.shortcuts import render,redirect
from app1.forms import registerform1,registerform2,registerform3
from django.http import HttpResponse
from .models import disease
def registerkal(request):
    if (request.method=='POST'):
     form=registerform1(request.POST)
     if form.is_valid():
       form.save()
       return redirect('home')
    else:
      form=registerform1()
      context={'form':form}
    return(render(request, "register.html",context))

def mom_vaccine(request):
    if(request.method=="POST"):
     form=registerform2(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form=registerform2()
        context={'form':form}
    return (render(request, 'register2.html',context))
def child(request):
    if(request.method=="POST"):
        form=registerform3(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=registerform3()
        context={'form':form}
    return (render(request, 'register3.html',context))
    
def home(request):
    # infant_diseases={'diseases':[
    #     {'name':"pollio_vaccine",'price':"120$"},
    #     {'name':"RTT_vaccine",'price':"250$"},
    #     {'name':"meningitis_vaccine",'price':"450$"},
    # ]}
    disease_names=disease.objects.all()
    disease_dict={'disdic':disease_names}
    return(render(request,"home.html",disease_dict))
# Create your views here.
