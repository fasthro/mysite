from django.db import models
from django.contrib.auth.models import AbstractUser

class BUser(AbstractUser):
    is_author = models.BooleanField(default=False, verbose_name='本站作者')
    head = models.CharField(max_length=200,default='', verbose_name="头像地址")
    introduction = models.CharField(max_length=200,default='', verbose_name="个人简介")
    github = models.CharField(max_length=200,default='', verbose_name="GitHub主页")


