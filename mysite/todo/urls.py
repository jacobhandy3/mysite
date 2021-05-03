from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListCreate, name='task-list'),
    path('<int:pk>', views.TaskDetail, name='task-detail'),
]