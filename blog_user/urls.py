from django.urls import path, re_path
from blog_user.views import SigninView, SignupView

app_name = 'blog_user'
urlpatterns = [
    re_path(r'^signin/$', SigninView.as_view(), name='signin'),
    re_path(r'^signup/$', SignupView.as_view(), name='signup'),
]