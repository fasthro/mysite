from django.shortcuts import render
from  django.http import HttpRequest
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from  django.template import Template

# Create your views here.

def index(request):
    t = get_template('./blog/index.html')
    html = t.render()
    return HttpResponse(html)