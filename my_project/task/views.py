from django.shortcuts import render
from .models import Task
from .models import Target


def get_home_page(request):
    tasks = Task.objects.all()

    return render(request, "task/home.html", {"tasks_list": tasks})

def get_target_page(request):
    target = Target.objects.all()

    return render(request, "task/home.html", {"list_targets": target})

def get_task(request, task_id):
    task_object = Task.objects.get(id=task_id)
    context = {
        "id": task_id,
        "object": task_object
    }
    return render(request, "task/task_view.html", context)