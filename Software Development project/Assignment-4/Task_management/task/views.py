from django.shortcuts import render,redirect
from . import forms
from . forms import Task_form
from . import models 
from .models import TaskModel 
# Create your views here.
def add_task(request):
    form=Task_form()

    if  request.method=='POST':
        form=Task_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('add_task')

    return render(request,'add_task.html',{'form':form})

def show_task(request):
    task=TaskModel.objects.all()
    return render(request, 'show_task.html', {"task": task})

def edit_task(request,id):
    tasks=models.TaskModel.objects.get(pk=id)
    edit_form=Task_form(instance=tasks)

    if  request.method=='POST':
        edit_form=forms.Task_form(request.POST,instance=tasks)

        if edit_form.is_valid():
            edit_form.save()
            return redirect('add_task')
    else:
        edit_form=forms.Task_form()
    edit_form=forms.Task_form(request.POST)
    return render(request,'add_task.html',{'form':edit_form})


def delete_task(request,id):
    form=models.TaskModel.objects.get(pk=id)
    form.delete()
    return redirect('show_task')