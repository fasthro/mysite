from datetime import datetime
from django.db import models
from django.conf import settings
from blog import conf
from blog import const
import os
import codecs

# 文章正文类型
ACT_HTML = 1      # html 内容
ACT_MD_TEXT = 2   # makedown 内容
ACT_MD_FILE = 3   # makedown 文件

ACT_CHOICES = {
    (ACT_HTML, "html"),
    (ACT_MD_TEXT, "md-text"),
    (ACT_MD_FILE, "md-file"),
}

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

    # 获取是否为空 tag
    def get_is_none(self):
        return self.tag_id == const.TAG_NONE_ID

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
    subtitle = models.CharField(max_length=100, default='', null=True, blank=True, verbose_name='文章副标题')
    img = models.CharField(max_length=200, default=conf.DEFAULT_ARTICLE_IMG_URL, verbose_name='展示图片')
    tags = models.ManyToManyField(ArticleTag, verbose_name='标签')
    abstract = models.TextField(verbose_name='文章摘要')
    content_type = models.IntegerField(default=ACT_HTML, choices=ACT_CHOICES, verbose_name='正文内容类型')
    content_file = models.FileField(upload_to=conf.get_article_content_file_upload_path, null=True, blank=True, verbose_name='正文文件路径')
    content = models.TextField(default='', null=True, blank=True, verbose_name='正文')
    create_time = models.DateTimeField(verbose_name='创建日期')
    modify_time = models.DateTimeField(default=datetime.now(), verbose_name='修改日期')
    praise_num = models.IntegerField(default=0, verbose_name='赞数量')
    comments_num = models.IntegerField(default=0, verbose_name='评论数量')
    browse_num = models.IntegerField(default=0, verbose_name='浏览数量')

    # 获取博客正文内容
    def get_content(self):
        if self.content_type == ACT_HTML or self.content_type == ACT_MD_TEXT:
            return self.content
        else:
            fp = self.content_file.path
            index = fp.find("static")
            if index != -1:
                sindex = index + len("static")
                fp = settings.STATIC_ROOT + fp[sindex:]
            if os.path.exists(fp):
                cont = codecs.open(fp, 'r', 'utf-8')
                text = ''
                for line in cont.readlines():
                    text = text + line
                return text
            else:
                return "content : none! " + fp;

    # 获取是否为 makedown 文档
    def get_is_md(self):
        return self.content_type == ACT_MD_TEXT or self.content_type == ACT_MD_FILE

    # 增加阅读数量
    def increase_browse(self):
        self.browse_num = self.browse_num + 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "article"
        verbose_name = '文章'
