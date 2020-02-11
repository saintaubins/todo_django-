from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos_list, name='todos_list'),
    path('update/', views.todos_update, name='todos_update')
]