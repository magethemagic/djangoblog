from django.contrib import admin

# Register your models here.
from apps.article.models import Article, Tag

admin.site.register(Article)
admin.site.register(Tag)