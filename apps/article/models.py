from django.db import models

# Create your models here.
from django.utils import timezone

from apps.user.models import UserProfile


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class Article(models.Model):
    created_date = models.DateTimeField(default=timezone.now, verbose_name='发布时间')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    content = models.CharField(max_length=140, verbose_name='内容')
    liked_num = models.IntegerField(default=0, verbose_name='点赞数')
    visited_num = models.IntegerField(default=0, verbose_name='浏览量')
    image = models.CharField(max_length=200, verbose_name='图片地址')

    tags = models.ManyToManyField(to=Tag)
    author = models.ForeignKey(to=UserProfile, on_delete=models.CASCADE, verbose_name='发布者id')

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'article'
        verbose_name = '文章表'
        verbose_name_plural = verbose_name
