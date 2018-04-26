from django.views.generic.list import ListView
from django.views.generic import DetailView
from  blog_user.models import BUser
from blog_article.models import Article, ArticleTag, ArticleType
from blog import conf


# base mixin
class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        tags = ArticleTag.objects.order_by('order')
        # 全局所有 tag 类型
        context['tags'] = tags
        # 导航 tags 对应的默认 tag 类型
        context['nav_tag'] = tags[0]

        # 全局所有 type 类型
        types = ArticleType.objects.order_by('order')
        # 全局所有 tag 类型
        context['types'] = types
        # 导航 types 对应的默认 type 类型
        context['nav_type'] = types[0]

        # 当前作者信息
        context['author'] = BUser.objects.get(is_author=True)
        return context


# home view
class MainView(BaseMixin, ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = conf.MAIN_PAGE_NUM


# types view
class TypesView(BaseMixin, ListView):
    model = Article
    template_name = 'blog/type.html'
    paginate_by = conf.MAIN_PAGE_NUM

    def get_queryset(self):
        tid = self.kwargs.get('type_id', '')
        at = ArticleType.objects.get(type_id=tid)
        return Article.objects.all().filter(type_id=at.id)

    def get_context_data(self, **kwargs):
        context = super(TypesView, self).get_context_data(**kwargs)
        # 当前选择的类型
        tid = self.kwargs.get('type_id', '')
        context['select_type'] = ArticleType.objects.get(type_id=tid)
        return context


# tags view
class TagsView(BaseMixin, ListView):
    model = Article
    template_name = 'blog/tags.html'
    paginate_by = conf.MAIN_PAGE_NUM

    def get_queryset(self):
        tag = self.kwargs.get('tag_id', '')
        return Article.objects.all().filter(tags__tag_id=tag)

    def get_context_data(self, **kwargs):
        context = super(TagsView, self).get_context_data(**kwargs)
        # 当前选择的标签
        context['select_tag'] = self.kwargs.get('tag_id', '')
        return context

