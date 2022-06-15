from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))