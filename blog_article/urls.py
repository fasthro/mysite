from django.urls import path, re_path
from blog_article.views import ArticleView

app_name = 'blog_article'
urlpatterns = [
    path('<int:pk>', ArticleView.as_view()),
]