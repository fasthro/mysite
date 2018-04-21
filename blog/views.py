from django.views.generic.list import ListView
from django.views.generic import DetailView
from  blog_user.models import BUser
from blog_article.models import Article, ArticleTag


# 主页
class MainView(ListView):
    model = Article
    template_name = "../templates/blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        # 全局所有 tag 类型
        context['tags'] = ArticleTag.objects.order_by('order')
        # 当前作者信息
        context['author'] = BUser.objects.get(is_author=True)
        return context
