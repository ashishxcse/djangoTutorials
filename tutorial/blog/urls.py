from django.urls import path
from . import views


urlpatterns = [
    path('temp/<int:id>/', views.temp)
]
