from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class UserProfile(AbstractUser):
    phone_number = models.CharField(max_length=11, verbose_name='电话号码', unique=True)
    user_avatar = models.CharField(max_length=500, verbose_name='头像地址')
    user_desc = models.CharField(max_length=140, verbose_name='个人信息')

    class Meta:
        db_table = 'user_profile'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
