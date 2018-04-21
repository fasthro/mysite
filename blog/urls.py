from django.urls import path
from blog.views import MainView

urlpatterns = [
    path('', MainView.as_view()),
]