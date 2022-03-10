from django.urls import path
from task import views

urlpatterns = [
    path('', views.get_home_page, name="home"),
    path('task_view/<int:task_id>', views.get_task, name="task_view"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),

]