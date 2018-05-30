from django.views.generic.list import ListView
from django.views.generic import DetailView
from blog_user.models import BUser
from blog_article.models import Article, ArticleTag, ArticleType
from blog import conf
from blog import const
from django.db.models import Q


# base mixin
class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(BaseMixin, self).get_context_data(**kwargs)
        tags = ArticleTag.objects.order_by('order')
        # 全局所有 tag 类型
        context['tags'] = tags
        # 导航 tags 对应的默认 tag 类型
        if len(tags) > 0:
            context['nav_tag'] = tags.filter(tag_id=const.TAG_NAV_ID)[0]
        else:
            context['nav_tag'] = None

        # 全局所有 type 类型
        types = ArticleType.objects.order_by('order')
        # 全局所有 tag 类型
        context['types'] = types
        # 导航 types 对应的默认 type 类型
        if len(types) > 0:
            context['nav_type'] = types.filter(type_id=const.TYPE_NAV_ID)[0]
        else:
            context['nav_type'] = None

        # 当前作者信息
        context['author'] = BUser.objects.get(is_author=True)
        return context


# home view
class MainView(BaseMixin, ListView):
    model = Article
    template_name = "blog/index.html"
    paginate_by = conf.MAIN_PAGE_NUM

    def get_queryset(self):
        at = ArticleType.objects.get(type_id=const.TYPE_MZ_ID)
        return Article.objects.all().filter(~Q(type_id=at.id))


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


# mz view
class MzView(BaseMixin, ListView):
    model = Article
    template_name = "blog/mz.html"

    def get_queryset(self):
        at = ArticleType.objects.get(type_id=const.TYPE_MZ_ID)
        return Article.objects.all().filter(type_id=at.id).order_by('-create_time')

    def get_context_data(self, **kwargs):
        context = super(MzView, self).get_context_data(**kwargs)
        self.get_group_list(context)
        return context

    # 获取分组
    def get_group_list(self, context):

        index = 0
        round2 = 0
        round3 = 0
        round4 = 0

        temps2_1 = []
        temps2_2 = []

        temps3_1 = []
        temps3_2 = []
        temps3_3 = []

        temps4_1 = []
        temps4_2 = []
        temps4_3 = []
        temps4_4 = []
        for item in self.object_list:
            index += 1

            # 2
            if index % 2 == 0:
                round2 += 1

            if index - round2 * 2 == 1:
                temps2_1.append(item)
            elif index - round2 * 2 == 0:
                temps2_2.append(item)

            # 3
            if index % 3 == 0:
                round3 += 1

            if index - round3 * 3 == 1:
                temps3_1.append(item)
            elif index - round3 * 3 == 2:
                temps3_2.append(item)
            elif index - round3 * 3 == 0:
                temps3_3.append(item)

            # 4
            if index % 4 == 0:
                round4 += 1

            if index - round4 * 4 == 1:
                temps4_1.append(item)
            elif index - round4 * 4 == 2:
                temps4_2.append(item)
            elif index - round4 * 4 == 3:
                temps4_3.append(item)
            elif index - round4 * 4 == 0:
                temps4_4.append(item)

        context['group_2_1'] = temps2_1
        context['group_2_2'] = temps2_2

        context['group_3_1'] = temps3_1
        context['group_3_2'] = temps3_2
        context['group_3_3'] = temps3_3

        context['group_4_1'] = temps4_1
        context['group_4_2'] = temps4_2
        context['group_4_3'] = temps4_3
        context['group_4_4'] = temps4_4

