from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Task
import json

def task_list(request):
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

def task_add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        task = Task.objects.create(title=title, description=description)
        return JsonResponse({"id": task.id, "title": task.title, "description": task.description})

def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Task, id=task_id)
        return JsonResponse({"id": task.id, "title": task.title, "description": task.description})

def task_update(request, task_id):
    if request.method == "PUT":
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.save()
        return JsonResponse({"id": task.id, "title": task.title, "description": task.description})

def task_delete(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({"message": "Task deleted successfully!"})
