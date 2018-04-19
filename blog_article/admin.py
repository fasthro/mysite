from django.contrib import admin

# Register your models here.

from blog_article import models

admin.register(models.BArticleCategory)
admin.register(models.BArticle)