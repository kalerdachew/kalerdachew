from django.urls import path,include
from .import views
urlpatterns = [
    path('registermom/',views.registerkal,name='registerm'),
    path('registermomvac/',views.mom_vaccine,name='momvac'),
    path('registerbab/',views.child,name='child'),
    path('home/',views.home,name='home'),
]
