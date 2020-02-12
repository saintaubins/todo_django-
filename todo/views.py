from django.shortcuts import render, redirect
from .models import Todo, List
from .forms import TodoForm, ListForm


def todos_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})


def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})


def todo_update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_form.html', {'form': form})


def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/todo_form.html', {'form': form})


def todo_delete(request, pk):
    Todo.objects.get(id=pk).delete()
    return redirect('todos_list')


# ***************


def task_list(request):
    tasks = List.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = List.objects.get(id=pk)
    return render(request, 'todo/task_detail.html', {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = ListForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_edit(request, pk):
    task = List.objects.get(pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = ListForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})


def task_delete(request, pk):
    List.objects.get(id=pk).delete()
    return redirect('task_list')
