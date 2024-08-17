from django.shortcuts import render, redirect
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

def update(request):
    return HttpResponse('The form is submitted')

def remove(request, item_id):
    Task.objects.filter(id=item_id).delete()  # This deletes the object(s) with the specified id
    messages.info(request, "item removed !!!")
    return redirect('')