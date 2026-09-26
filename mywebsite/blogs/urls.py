from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('allposts/', views.blogposts, name='blogposts'),
    path('allposts/<blog>/', views.blog_post, name='blog_post'),
]
