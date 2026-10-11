from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('filter/', views.task_filter, name='task_filter'),
    path('load-more/', views.task_load_more, name='task_load_more'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
