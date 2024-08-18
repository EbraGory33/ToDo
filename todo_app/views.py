from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from django.contrib import messages
# Create your views here.

def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_on')
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }
    return render(request, 'home.html', context)

############################################################################################################################
def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_incomplete(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.save()
    return redirect('home')

def remove(request, pk):
    Task.objects.filter(pk=pk).delete()  # This deletes the object(s) with the specified id
    messages.info(request, "item removed !!!")
    return redirect('home')