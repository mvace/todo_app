from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from .forms import TaskForm


class TaskListCreate(View):
    template_name = "todo/task_list.html"

    def get(self, request):
        tasks = Task.objects.all().order_by("finished", "created_at")
        form = TaskForm()
        return render(request, self.template_name, {"tasks": tasks, "form": form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tasks")
        tasks = Task.objects.all().order_by("finished", "created_at")
        return render(request, self.template_name, {"tasks": tasks, "form": form})


class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "finished"]
    success_url = reverse_lazy("todo:tasks")


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:tasks")


def toggle_finished(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.finished = not task.finished
    task.save()
    return redirect("todo:tasks")
