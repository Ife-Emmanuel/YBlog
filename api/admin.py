from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('id', 'title', 'description')

