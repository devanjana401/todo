from django.shortcuts import render,redirect
from.models import Task
# Create your views here.
def home(request):
    task=Task.objects.filter(is_completed=False)
    completed=Task.objects.filter(is_completed=True)
    context={
        'task':task,
        'completed':completed,
    }
    return render(request,'home.html',context)
def add_task(request):
    if request.method=='POST':
        task=request.POST.get('task')
        Todo=Task.objects.create(task=task)
        Todo.save()
        return redirect('home')
def mark_done(request,task_id):
    task=Task.objects.get(id=task_id)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_undone(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')