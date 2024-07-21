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

    def get_session_key(self, request):
        if not request.session.session_key:
            request.session.create()
        return request.session.session_key

    def get(self, request):
        session_key = self.get_session_key(request)
        tasks = Task.objects.filter(session_key=session_key).order_by(
            "finished", "created_at"
        )
        form = TaskForm()
        return render(request, self.template_name, {"tasks": tasks, "form": form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.session_key = self.get_session_key(request)
            form.save()
            return redirect("todo:tasks")
        tasks = Task.objects.all().order_by("finished", "created_at")
        return render(request, self.template_name, {"tasks": tasks, "form": form})


class TaskUpdate(UpdateView):
    model = Task
    fields = ["title", "finished"]
    success_url = reverse_lazy("todo:tasks")

    def get_queryset(self):
        session_key = self.request.session.session_key
        return Task.objects.filter(session_key=session_key)


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:tasks")

    def get_queryset(self):
        session_key = self.request.session.session_key
        return Task.objects.filter(session_key=session_key)


def toggle_finished(request, pk):
    session_key = request.session.session_key
    task = get_object_or_404(Task, pk=pk, session_key=session_key)
    task.finished = not task.finished
    task.save()
    return redirect("todo:tasks")
