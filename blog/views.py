from django.views.generic.list import ListView
from django.views.generic import DetailView
from  blog_user.models import BUser
from blog_article.models import Article, ArticleTag
from blog import conf


# home view
class MainView(ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = conf.MAIN_PAGE_NUM

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        tags = ArticleTag.objects.order_by('order')
        # 全局所有 tag 类型
        context['tags'] = tags
        # 导航 tags 对应的默认 tag 类型
        context['nav_tag'] = tags[0]
        # 当前作者信息
        context['author'] = BUser.objects.get(is_author=True)
        return context


# tags view
class TagsView(ListView):
    model = Article
    template_name = 'blog/tags.html'
    paginate_by = conf.MAIN_PAGE_NUM

    def get_queryset(self):
        tag = self.kwargs.get('tag_id', '')
        return Article.objects.all().filter(tags__regex=tag)

    def get_context_data(self,**kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        tags = ArticleTag.objects.order_by('order')
        # 全局所有 tag 类型
        context['tags'] = tags
        # 导航 tags 对应的默认 tag 类型
        context['nav_tag'] = tags[0]
        return context
