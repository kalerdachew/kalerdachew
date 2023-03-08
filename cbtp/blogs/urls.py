from django.urls import path,include
from .views import blogview
urlpatterns = [
    path('new/',blogview.as_view()),
]
