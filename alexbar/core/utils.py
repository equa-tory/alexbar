from .models import *

headers = [
    {'id': 'en', 'title': 'About', 'url':'about'},
    {'id': 'en', 'title': 'Ideas', 'url':'ideas'},
    {'id': 'ru', 'title': 'Обо мне', 'url':'about'},
    {'id': 'ru', 'title': 'Идеи', 'url':'ideas'},
]

sections = []
for s in Section.objects.all():
    sections.append({
        'name': s.name,
        'categories': s.categories.all()
    })

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['headers'] = headers
        context['sections'] = sections
        
        return context
