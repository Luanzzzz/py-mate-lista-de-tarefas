from django import forms

from .models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "completed", "tags")
        widgets = {
            "content": forms.TextInput(attrs={"placeholder": "Ex.: Comprar mantimentos"}),
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": forms.CheckboxSelectMultiple,
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ("name",)
        widgets = {"name": forms.TextInput(attrs={"placeholder": "Ex.: trabalho"})}
