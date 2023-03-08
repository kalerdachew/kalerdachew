from django.urls import path
from .import views
from .views import (
    feed_list,
    feed_deatil,
    create_feeds,
    update_feeds,
    delete_feeds)
urlpatterns = [
    path('',views.home,name="magazine-home"),
    path('feeds/',feed_list.as_view(),name="magazine-feed"),
    path('feeds/<int:pk>/',feed_deatil.as_view(template_name='detail.html'),name="magazine_detail"),
    path('feeds/<int:pk>/update/',update_feeds.as_view(template_name='create.html'),name="magazine_update"),
    path('feeds/new/',create_feeds.as_view(template_name='create.html'),name="magazine_new"),
     path('feeds/<int:pk>/delete/',delete_feeds.as_view(template_name='feed_delete_confirm.html'),name="magazine_delete"),
    # path('index/',views.index,name="magazine-index"),
    # path('<int:Article_id>/',views.result,name="maga-result") ,  #using int to show the parameter format
    # path('info/',views.information),
    # path('setform/',views.setform),
    # path('getform/',views.getform,name='getform')
]
