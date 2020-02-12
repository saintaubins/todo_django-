from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('update/', views.todo_update, name='todo_update'),
    path('todos/<int:pk>/', views.todo_detail, name='todo_detail'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/new/', views.todo_create, name='todo_create'),

    path('tasks/', views.task_list, name= 'task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete')
]


