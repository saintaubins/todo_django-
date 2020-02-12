from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('update/', views.todos_update, name='todos_update'),
    path('todos/<int:pk>/', views.todos_detail, name='todos_detail'),
    path('todos/<int:pk>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/new/', views.todo_create, name='todo_create')
]


