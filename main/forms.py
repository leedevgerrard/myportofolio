from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Project, Experience

class ProjectForm(ModelForm):
  class Meta:
    model = Project
    fields = [
      "title",
      "description",
      "thumbnail",
      "thumbnail_alt",
    ]

    labels = {
      "title": "Project Name",
      "description": "Project Description",
      "thumbnail": "Project Image URL",
      "thumbnail_alt": "Project Image Alt",
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
      "thumbnail_alt": TextInput(
        attrs={
          "placeholder": "Logo of Portfolio Website",
          "maxlength": 255,
        }
      ),
    }

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