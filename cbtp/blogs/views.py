from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import blogs
class blogview(CreateView):
 model= blogs
 template_name='blog.html'
 fields= "__all__"
 
