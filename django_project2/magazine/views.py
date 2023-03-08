from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from .models import Article,Reporter
from users.models import profile
from django.contrib.auth.models import User
from magazine.forms import Form
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

#from django
# Create your views here.
def home(request):
    return(render(request, 'home.html',{'title':'home'}))
@login_required()
def feed(request):
    items={
        'articles':Article.objects.all()
    }
    return(render(request, 'feeds.html',items))

    #bloging the magazine using Listview(class based view)
class feed_list(ListView):
    model=Article
    template_name='feeds.html'
    context_object_name='articles'
    ordering=['date']

class feed_deatil(DetailView):
   model=Article
  # template_name='detail.html'
   #context_object_name='articles'


class create_feeds(LoginRequiredMixin,CreateView):
    model=Article
    fields=['Title','reporter']
    #template_name='create.html'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class update_feeds(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Article
    fields=['Title','reporter']
  #  template_name='create.html'
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        Article=self.get_object()   #getting the Article object from models.py file
        if self.request.user==Article.reporter:
            return True
        return False

class delete_feeds(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Article
    def test_func(self):
     Article=self.get_object()
     if self.request.user==Article.reporter:
       return True
     return False




# def result(requset,Article_id):
#     article=get_object_or_404(Article,pk=Article_id)      #using get_object_or _404 from django.shortcuts
#     return (HttpResponse('Your Article id is %s.'%Article_id))
# def index(request):
#     rep=Form
#     redirect('magazine-feed')
#     return(render(request, 'index.html',{'form':rep}))
# def information(request):
#     path=request.path
#     scheme=request.scheme
#     method=request.method
#     informatics= f''' request.path={path},
#     request.scheme={scheme},
#     request.method={method}
#      ''' 
#     return(HttpResponse(informatics))
# def setform(request):
#     return(render(request, 'form.html'))
# def getform(request):
#      if request.method=='POST':
#         id=request.POST['id']
#         name=request.POST['name']
#         return(HttpResponse(name,id))