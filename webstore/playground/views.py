from django.shortcuts import render

from django.http import HttpResponse
def calculate():
    x=34
    y=77
    return y
def view1(request):
    x=1
    y=calculate()
    return render(request, 'hello.html',{'name':'kirubel'})
