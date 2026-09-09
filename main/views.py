from django.shortcuts import render

from main.models import Experience


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
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)