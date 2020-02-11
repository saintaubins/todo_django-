from django.shortcuts import render, redirect
from .models import Todos
from .forms import TodosForm

def todos_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo/todos_list.html', {'todos': todos})


def todos_update(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos_list')
    else:
        form = TodosForm()
    return render(request, 'todo/todos_update.html', {'form': form})

