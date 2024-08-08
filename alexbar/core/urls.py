from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('redir',views.redir,name='redir'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('ideas',views.ideas,name='ideas'),

    # posts
    path('little-giant',views.little_giant,name='little-giant'),
    path('katastasis',views.katastasis,name='katastasis'),
]
