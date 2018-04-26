from datetime import datetime
from django.db import models
from django.conf import settings
from blog import conf


# 文章标签定义
class ArticleTag(models.Model):
    tag_id = models.CharField(max_length=40, verbose_name="标签标识Id")
    name = models.CharField(max_length=40, verbose_name="标签名称")
    order = models.IntegerField(default=0, verbose_name="标签顺序")
    LABEL_STYLE = (
        ("label-success", "label-success"),
        ("label-info", "label-info"),
        ("label-warning", "label-warning"),
        ("label-danger", "label-danger"),
    )
    tag_label_style = models.CharField(max_length=200, choices=LABEL_STYLE, default='label-success', verbose_name='标签样式')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "article_tag"
        verbose_name = '文章标签'


# 文章标签定义
class ArticleType(models.Model):
    type_id = models.CharField(max_length=40, verbose_name="类型标识Id")
    name = models.CharField(max_length=40, verbose_name="类型名称")
    order = models.IntegerField(default=0, verbose_name="类型顺序")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "article_type"
        verbose_name = '文章类型'


# 文章数据模型
class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    type = models.ForeignKey(ArticleType, verbose_name='文章类型', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='文章标题')
    subtitle = models.CharField(max_length=100, default='', verbose_name='文章副标题')
    img = models.CharField(max_length=200, default=conf.DEFAULT_ARTICLE_IMG_URL, verbose_name='展示图片')
    tags = models.ManyToManyField(ArticleTag, verbose_name='标签')
    abstract = models.TextField(verbose_name='文章摘要')
    content = models.TextField(verbose_name='正文')
    create_time = models.DateTimeField(verbose_name='创建日期')
    modify_time = models.DateTimeField(default=datetime.now(), verbose_name='修改日期')
    praise_num = models.IntegerField(default=0, verbose_name='赞数量')
    comments_num = models.IntegerField(default=0, verbose_name='评论数量')
    browse_num = models.IntegerField(default=0, verbose_name='浏览数量')

    # 增加阅读数量
    def increase_browse(self):
        self.browse_num = self.browse_num + 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"
        verbose_name = '文章'
