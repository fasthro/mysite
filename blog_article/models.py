from django.db import models
from django.conf import settings


class BArticleCategory(models.Model):
    '''
    文章分类数据模型
    '''
    name = models.CharField(max_length=40, verbose_name="类型名称")
    order = models.IntegerField(default=0, verbose_name="类型顺序")

class BArticle(models.Model):
    '''
    文章数据模型
    '''
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    category = models.ForeignKey(BArticleCategory, verbose_name='文章类型', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='文章标题')
    img = models.CharField(max_length=200, verbose_name='展示图片')
    tags = models.CharField(max_length=200, verbose_name='标签', help_text='多个用|分割')
    abstract = models.TextField(verbose_name='文章摘要')
    content = models.TextField(verbose_name='正文')
    create_time = models.IntegerField(default=0, verbose_name='创建日期')
    praise_num = models.IntegerField(default=0, verbose_name='赞数量')
    comments_num = models.IntegerField(default=0, verbose_name='评论数量')
    browse_num = models.IntegerField(default=0, verbose_name='浏览数量')