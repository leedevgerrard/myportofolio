from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

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