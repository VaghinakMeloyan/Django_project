from django.urls import path
from task import views


urlpatterns = [
    path("", views.get_home_page, name="home"),
    path("task_view/<int:task_id>", views.get_task, name="task-view"),
    path("task_delete/<int:task_id>", views.delete_task, name="task-delete")
]