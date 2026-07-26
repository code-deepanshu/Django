from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new task to the database!
            return redirect('home')
    else:
        form = TaskForm()

    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


from django.shortcuts import render, redirect, get_object_or_404

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')