from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput, NumberInput, CharField

from main.models import Project, Experience

class ProjectForm(ModelForm):
  goals = CharField(
    required=False,
    widget=Textarea(
      attrs={
        "placeholder": "Enter each goal on a new line",
        "rows": 3,
      }
    ),
  )

  class Meta:
    model = Project
    fields = [
      "title",
      "description",
      "thumbnail",
      "screenshot",
      "year",
      "role",
      "stack",
      "problem",
      "goals",
    ]

    labels = {
      "title": "Project Title",
      "description": "Description",
      "thumbnail": "Project Logo URL",
      "screenshot": "Project Screenshot URL",
      "year": "Year",
      "role": "My Role",
      "stack": "Tech Stack",
      "problem": "Problem Statement",
      "goals": "Project Goals",
    }

    widgets = {
      "title": TextInput(
        attrs={
          "placeholder": "Portfolio Website",
          "maxlength": 255,
        }
      ),
      "description": Textarea(
        attrs={
          "placeholder": "Describe your project",
          "rows": 3,
        }
      ),
      "thumbnail": URLInput(
        attrs={
          "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
        }
      ),
      "screenshot": URLInput(
        attrs={
          "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
        }
      ),
      "year": NumberInput(
        attrs={
          "min": 2000,
          "max": 2026,
        }
      ),
      "role": TextInput(
        attrs={
          "placeholder": "Full Stack Developer",
          "maxlength": 255,
        }
      ),
      "stack": TextInput(
        attrs={
          "placeholder": "MERN",
          "maxlength": 255,
        }
      ),
      "problem": Textarea(
        attrs={
          "placeholder": "Define your problem statement",
          "rows": 3,
        }
      ),
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    if self.instance.pk:
      self.initial["goals"] = "\n".join(self.instance.goals or [])

  def clean_goals(self):
    goals = self.cleaned_data["goals"]

    return [
      goal.strip()
      for goal in goals.splitlines()
      if goal.strip()
    ]

class ExperienceForm(ModelForm):
  class Meta:
    model = Experience
    fields = [
      "title",
      "description",
      "category",
      "start_date",
      "end_date",
    ]

    labels = {
      "title": "Experience Name",
      "description": "Experience Description",
      "category": "Experience Category",
      "start_date": "Experience Start Date",
      "end_date": "Experience End Date"
    }

    widgets = {
      "title": TextInput(
        attrs={
          "placeholder": "Web Dev Intern",
          "maxlength": 255,
        }
      ),
      "description": Textarea(
        attrs={
          "placeholder": "Describe your experience",
          "rows": 3,
        }
      ),
      "start_date": DateInput(
        attrs={
          "type": "date",
          "class": "date-input",
          "min": "2000-01-01",
          "max": "2026-12-31",
        }
      ),
      "end_date": DateInput(
        attrs={
          "type": "date",
          "class": "date-input",
        }
      )
    }