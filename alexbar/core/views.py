from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import Template, Context
from django.utils.safestring import mark_safe

from core.utils import *
from .models import *


from .main import convert_to_html


def redir(request):
    return redirect('index')

def index(request):
    framer1 = []
    framer2 = []
    framer3 = []
    # frames = [framer1, framer2, framer3]

    posts = Post.objects.all().order_by('-position')
    for i, p in enumerate(posts):
        if i % 3 == 0:
            framer1.append(p)
        elif i % 3 == 1:
            framer2.append(p)
        else:
            framer3.append(p)
        # target_array = frames[i % len(frames)]
        # target_array.append(p)

    data = {
        'title': 'Alex Barauskas',
        'headers': headers,
        'sections': sections,
        'posts': posts,

        'framer1': framer1,
        'framer2': framer2,
        'framer3': framer3
    }
    return render(request, 'core/index.html', context=data)

def about(request):
    data = {
        'title': 'About',
        'headers': headers,
        'sections': sections
    }
    return render(request, 'core/about.html', context=data)

def ideas(request):
    ideas = Idea.objects.all().order_by('date')
    data = {
        'title': 'Ideas',
        'headers': headers,
        'sections': sections,
        'ideas': ideas
    }
    return render(request, 'core/ideas.html', context=data)

def pageNotFound(request, exception):
    data = {
        'title': '404',
        'headers': headers,
        'sections': sections
    }
    return render(request, 'core/404.html', context=data)

# ============================================================
# POSTS

def post(request, slug):
    post = Post.objects.get(slug=slug)
    
    if post.has_html:
        data = {
            'title': post.name,
            'headers': headers,
            'sections': sections,
        }
        return render(request, f'core/posts/{post.slug}.html', context=data)

    else:

        content = convert_to_html(post.content)
        template = Template(content)

        context = {

            'title': post.name,
            'headers': headers,
            'sections': sections,
        }

        pre_render = template.render(Context(context))

        data = {
            'content': mark_safe(pre_render),
        }
        return render(request, f'core/posts/post.html', context=data)