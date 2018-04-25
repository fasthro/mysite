from django.views.generic.detail import DetailView
from blog_article.models import Article, ArticleTag, ArticleType


# article view
class ArticleView(DetailView):
    model = Article
    template_name = 'blog_article/article.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(ArticleView, self).get(request, *args, **kwargs)
        self.object.increase_browse()
        return response

    def get_object(self, queryset=None):
        article = super(ArticleView, self).get_object(queryset)
        return article




