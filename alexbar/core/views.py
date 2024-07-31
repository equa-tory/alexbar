from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.utils import *

def redir(request):
    return redirect('index')

def index(request):
    data = {
        'title': 'Alex Barauskas',
        'menus': menus
    }
    return render(request, 'core/index.html', context=data)

def about(request):
    data = {
        'title': 'About',
        'menus': menus
    }
    return render(request, 'core/about.html', context=data)

def ideas(request):
    data = {
        'title': 'Ideas',
        'menus': menus
    }
    return render(request, 'core/ideas.html', context=data)

def pageNotFound(request, exception):
    data = {
        'title': '404',
        'menus': menus
    }
    return render(request, 'core/404.html', context=data)