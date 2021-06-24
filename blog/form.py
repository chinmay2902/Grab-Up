from django import forms
from django.forms import fields
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields="__all__"

