# Create your views here.
from datetime import date

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from apps.article.models import Article
from apps.user.models import UserProfile


def check_user(func):
    def inner(*args, **kwargs):
        username = args[0].session.get("username", "")
        if username == "":
            args[0].session['path'] = args[0].path
            return redirect(reverse("user:login"))
        return func(*args, **kwargs)

    return inner


@check_user
def upload_article(request):
    print(request)
    author = request.GET.get('author')
    user = UserProfile.objects.filter(username=author).first()
    content = request.GET.get('content')
    blog = Article.objects.create(content=content, author=user)
    if blog:
        data = {'status': 1}
    else:
        data = {'status': 0}
    return JsonResponse(data)


def show_blog(request):
    data = {}
    articles = Article.objects.values()
    data['list'] = list(articles)
    return JsonResponse(data)
