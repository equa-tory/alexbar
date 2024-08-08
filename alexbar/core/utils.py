from .models import *

headers = [
    {'title': 'About', 'url':'about'},
    {'title': 'Ideas', 'url':'ideas'},
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
