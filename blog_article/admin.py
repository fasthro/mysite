from django.contrib import admin

# Register your models here.

from blog_article import models

admin.site.register(models.ArticleTag)
admin.site.register(models.ArticleType)
admin.site.register(models.Article)