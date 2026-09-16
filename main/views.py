from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project
from main.forms import ProjectForm


def show_main(request):
    context = {
        "name": "Lee Devin Gerrard",
        "npm": "2506548452",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
          "I am a highly motivated Computer Science student at Universitas Indonesia. "
          "I love learning new things, building things, breaking things, "
          "and figuring out why they work the way they do. I'm currently "
          "discovering the world of cybersecurity and AI."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Lee Devin Gerrard",
        "experience_list": Experience.objects.order_by("-start_date"),
    }
    return render(request, "experience.html", context)


def show_project(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Lee Devin Gerrard",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)


def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added successfully!")
        return redirect("main:show_project")

    context = {
        "name": "Lee Devin Gerrard",
        "form": form,
    }
    return render(request, "projects_form.html", context)


def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")


def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")