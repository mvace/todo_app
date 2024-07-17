from django.urls import path

from .views import TaskList, TaskDetail, TaskDelete

app_name = "todo"

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>", TaskDetail.as_view(), name="task-detail"),
    path("task/delete/<int:pk>", TaskDelete.as_view(), name="task-delete"),
]
