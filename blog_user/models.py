from django.db import models
from django.contrib.auth.models import AbstractUser
from blog import conf

class BUser(AbstractUser):
    '''
    数据模型
    '''

    is_author = models.BooleanField(default=False, verbose_name='本站作者')
    head = models.CharField(max_length=200, default=conf.DEFAULT_HEAD_URL, verbose_name="头像地址")
    introduction = models.CharField(max_length=200, default=conf.DEFAULT_INTRODUCTION, verbose_name="个人简介")
    github = models.CharField(max_length=200, default=conf.DEFAULT_GITHUB_URL, verbose_name="GitHub主页")

    class Meta:
        db_table = "user"
        verbose_name = 'User'


