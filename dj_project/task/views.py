from django.shortcuts import render, HttpResponse, redirect
from .models import Task
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def get_home_page(request):
    tasks = Task.objects.all()
    return render(request, "tasks/home.html", {"task_list": tasks})

def get_task(request, task_id):

    task_object = Task.objects.get(id=task_id)
    context = {
        "task_id": task_id,
        "task_obj": task_object,
    }
    return render(request, "tasks/task_view.html", context)

def update(request, id):

    task_object = Task.objects.get(id=id)
    context = {
        "id": id,
        "task_object": task_object,
    }
    return render(request, "tasks/home.html", context)

def delete(request, id):
    task_object = Task.objects.get(id=id)
    task_object.delete()
    return render(request, "tasks/home.html")




