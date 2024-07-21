from django.urls import path

from .views import TaskListCreate, TaskDelete, TaskUpdate, toggle_finished

app_name = "todo"

urlpatterns = [
    path("", TaskListCreate.as_view(), name="tasks"),
    path("task/delete/<int:pk>", TaskDelete.as_view(), name="task-delete"),
    path("task/toggle/<int:pk>", toggle_finished, name="toggle-task-finished"),
    path("task/update/<int:pk>", TaskUpdate.as_view(), name="task-update"),
]
