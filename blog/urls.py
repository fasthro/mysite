from django.urls import path, re_path
from blog.views import MainView
from blog.views import TagsView
from blog.views import TypesView
from blog.views import MzView

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', MainView.as_view(), name='home'),
    re_path('^tags/(?P<tag_id>\w+)/$', TagsView.as_view(), name='tags'),
    re_path('^types/(?P<type_id>\w+)/$', TypesView.as_view(), name='types'),
    re_path(r'^mz/$', MzView.as_view(), name='mz'),
]
