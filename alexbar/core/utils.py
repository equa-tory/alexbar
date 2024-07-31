menus = [
    {'type': 'title', 'title': 'About', 'url':'about'},
    {'type': 'title', 'title': 'Ideas', 'url':'ideas'},
    {'type': 'menu', 'title': 'Games', 'url':'#'},
    {'type': 'contact', 'title': 'Discord', 'url':'#'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menus'] = menus
        
        return context
