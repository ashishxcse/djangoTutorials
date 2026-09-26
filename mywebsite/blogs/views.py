from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def home_page(request):
    return HttpResponse("Homepage")

def blogposts(request):
    return HttpResponse("all posts")

# def python_intro(request):
#     return HttpResponse("Python Intro")

# def Django_intro(request):
#     return HttpResponse("Django Intro")

blog_names = {
    'python-intro': '<h1> Python Post </h1>',
    'django-intro': '<h1> Django Post </h1>',
    'sql-intro': '<h1> SQL Post </h1>'
}

def blog_post(request, blog):
    try:
        res = blog_names[blog]

    except Exception:
        return HttpResponseNotFound("<h1>Blog not found</h1>")

    else:
        return HttpResponse(res)
