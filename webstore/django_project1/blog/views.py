from django.shortcuts import render
from django.http import HttpResponse
from .models import post

products=[
    {
        'title':'Blog post1',
        'author':'coreyMs',
        'date':'august 12,2010',
        'content':'first blog content'
    },
    {
        'title':'Blog post2',
        'author':'Dane Joe',
        'date':'february 26,2022',
        'content':'second blog content'
    }
]
def home(request):
     return render(request, 'home.html',{'title':'home'})
def log(request):
       items={
        'posts':post.objects.all()
     }
       return render(request, 'log.html',items)
