from django.shortcuts import render, redirect
from .models import Task



def get_home_page(request):
    tasks = Task.objects.all()

    return render(request, "task/home.html", {"tasks_list": tasks})



def get_task(request, task_id):
    task_object = Task.objects.get(id=task_id)
    context = {
        "task_id": task_id,
        "task_object": task_object
    }
    return render(request, "task/task_view.html", context)

def delete_task(request, task_id):
    try:
        task = Task.objeqts.get(id=task_id)
    except Task.DoesNotExist:
        return redirect("home")

    task.delete()
    return redirect("home")