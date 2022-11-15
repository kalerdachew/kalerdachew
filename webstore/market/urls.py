from django.urls import include,path
from .import views
urlpatterns = [
    path('request/',views.response)
]
