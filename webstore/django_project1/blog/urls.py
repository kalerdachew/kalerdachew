from django.urls import include,path
from . import views
urlpatterns = [
   path('',views.home,name='blog-home'),
   path('log/',views.log,name='blog-log')
]