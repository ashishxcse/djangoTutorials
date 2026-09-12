from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def home_page(request):
    return HttpResponse("Homepage")

def blogposts(request):
    return HttpResponse("all posts")

# def python_intro(request):
#     return HttpResponse("Python Intro")

# def Django_intro(request):
#     return HttpResponse("Django Intro")

def blog_post(request, slug):
    if slug == 'python-intro':
        res = "Python Post"

    elif slug == 'django-intro':
        res = 'Django Post'

    return HttpResponse(res)
