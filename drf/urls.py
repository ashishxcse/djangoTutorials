from django.urls import path
from . import views

urlpatterns = [
    path('get/<int:id>', views.get_student, name='get_student'),
    path('list/', views.list_student, name='list_student'),
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:id>', views.delete_student, name='delete_student'),
    path('update/<int:id>', views.update_student, name='update_student'),
]
