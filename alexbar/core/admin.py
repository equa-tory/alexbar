from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = ['name',]

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name',]

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = [
        'name',
        'description', 
        'position',
        'date',
        'preview_image',
        'small_preview',
        'slug', 
        'category',
    ]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category',)
    ordering = ['position']

class IdeaAdmin(admin.ModelAdmin):
    model = Idea
    list_display = ['name', 'date']
    ordering = ['date']

admin.site.register(Section, SectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Idea, IdeaAdmin)