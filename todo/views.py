from django.shortcuts import render

from .models import Todos

def todos_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo/todos_list.html', {'todos': todos})


