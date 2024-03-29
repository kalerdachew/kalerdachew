"""django_project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
from users import views as user_view
from django.conf import settings #####
from django.conf.urls.static import static ######
#from .import views as user_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('magazine/',include('magazine.urls')),
    path('register/',user_view.register,name="register"),
    path('profile/',user_view.profile,name="user-profile"),
    path('login/',auth_view.LoginView.as_view(template_name="login.html"),name="login"),
    path('logout/',auth_view.LogoutView.as_view(template_name="logout.html"),name="logout"),
    path('profile_demo/',include('users.urls')),
] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)      #used for serving files uploaded by the User
