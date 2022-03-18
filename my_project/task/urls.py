from django.urls import path
from task import views


urlpatterns = [
    path("", views.get_home_page, name="home"),
    path("target/", views.get_target_page, name="home_1"),
    path("task_view/<int:task_id>", views.get_task, name="task-view")
]