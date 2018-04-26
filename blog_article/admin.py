from django.contrib import admin
from blog_article import models

# list_display =[] 设置显示在列表中的字段
# ordering = [] 在列表中的排序规则
# list_editable = [] 设置可编辑的字段

@admin.register(models.ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag_id', 'order']
    ordering = ['-order']


@admin.register(models.ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type_id', 'order']
    ordering = ['-order']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'create_time']
    ordering = ['-create_time']
    list_editable = ['type']
    filter_horizontal = ('tags',)
