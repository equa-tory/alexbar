from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('redir',views.redir,name='redir'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('ideas',views.ideas,name='ideas'),

    # posts
    path('post/<slug>',views.post,name='post'),
]