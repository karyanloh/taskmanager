from django import forms
from .models import Project


class CreateFrom(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "owner",
        ]
