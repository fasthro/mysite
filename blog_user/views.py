from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from blog_user.models import BUser


# sign in view
class SigninView(TemplateView):
    model = BUser
    template_name = 'blog_user/signin.html'


# sign up view
class SignupView(TemplateView):
    model = BUser
    template_name = 'blog_user/signup.html'

