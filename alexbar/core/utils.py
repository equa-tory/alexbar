menus = [
    {'title': 'About', 'url':'about'},
    {'title': 'Ideas', 'url':'ideas'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menus'] = menus
        
        return context
