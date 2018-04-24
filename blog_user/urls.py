from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('signin/', TemplateView.as_view(template_name="../templates/blog/signin.html")),
    path('signup/', TemplateView.as_view(template_name="../templates/blog/signup.html")),
]