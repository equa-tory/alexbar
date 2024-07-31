from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('',views.index,'redir'),
    path('about',views.about,name='about'),
    path('ideas',views.ideas,name='ideas'),
]
