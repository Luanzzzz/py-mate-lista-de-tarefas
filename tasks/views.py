from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TagForm, TaskForm
from .models import Tag, Task


def task_list(request):
    tasks = Task.objects.prefetch_related("tags").order_by("completed", "-created_at")
    return render(request, "tasks/task_list.html", {"tasks": tasks})


def task_create(request):
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:task_list")
    return render(request, "tasks/form.html", {"form": form, "title": "Nova tarefa", "cancel_url": "tasks:task_list"})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:task_list")
    return render(request, "tasks/form.html", {"form": form, "title": "Atualizar tarefa", "cancel_url": "tasks:task_list"})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")
    return render(request, "tasks/confirm_delete.html", {"object": task, "object_type": "tarefa", "cancel_url": "tasks:task_list"})


@require_POST
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect("tasks:task_list")


def tag_list(request):
    return render(request, "tasks/tag_list.html", {"tags": Tag.objects.all()})


def tag_create(request):
    form = TagForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:tag_list")
    return render(request, "tasks/form.html", {"form": form, "title": "Nova tag", "cancel_url": "tasks:tag_list"})


def tag_update(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    form = TagForm(request.POST or None, instance=tag)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("tasks:tag_list")
    return render(request, "tasks/form.html", {"form": form, "title": "Atualizar tag", "cancel_url": "tasks:tag_list"})


def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == "POST":
        tag.delete()
        return redirect("tasks:tag_list")
    return render(request, "tasks/confirm_delete.html", {"object": tag, "type": "tag", "cancel_url": "tasks:tag_list"})
