# pages/views.py
from django.shortcuts import rendergitgit
from django.http import HttpResponse

# Create your views here.

def homePageView(request):
    return HttpResponse('Hello, World!')
