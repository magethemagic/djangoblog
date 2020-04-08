from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^post', views.upload_article, name='post'),
    url(r'^show', views.show_blog, name='show')
]
