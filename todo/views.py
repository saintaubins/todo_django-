from django.shortcuts import render, redirect
from .models import Todos, Lists
from .forms import TodosForm, ListsForm


def todos_list(request):
    todos = Todos.objects.all()
    return render(request, 'todo/todos_list.html', {'todos': todos})


def todos_detail(request, pk):
    todos = Todos.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todos': todos})


def todos_update(request, pk):
    todo = Todos.objects.get(pk=pk)
    if request.method == 'POST':
        form = TodosForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos_list', pk=todo.pk)
    else:
        form = TodosForm(instance=todo)
    return render(request, 'todo/todos_form.html', {'form': form})

def todo_create(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():
            todos = form.save()
            return redirect('todos_detail', pk=todos.pk)
    else:
        form = TodosForm()
    return render(request, 'todo/todos_form.html', {'form': form})

def todo_delete(request, pk):
    Todos.objects.get(id=pk).delete()
    return redirect('todos_list')



# ***************



def list_list(request):
    lists = Lists.objects.all()
    return render(request, 'todo/list_list.html', {'lists': lists})


def list_detail(request, pk):
    lists = Lists.objects.get(id=pk)
    return render(request, 'todo/list_detail.html', {'lists': lists})



def list_create(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            listts = form.save()
            return redirect('list_detail', pk=listts.pk)
    else:
        form = ListForm()
    return render(request, 'todo/list_form.html', {'form': form})



def list_edit(request, pk):
    listts = Lists.objects.get(pk=pk)
    if request.method == "POST":
        form = ListForm(request.POST, instance=listts)
        if form.is_valid():
            listts = form.save()
            return redirect('stat_detail', pk=listts.pk)
    else:
        form = ListForm(instance=listts)
    return render(request, 'todo/list_form.html', {'form': form})



def list_delete(request, pk):
    Lists.objects.get(id=pk).delete()
    return redirect('list_list')
