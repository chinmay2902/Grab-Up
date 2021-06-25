from django import forms
from django.forms import fields, models
from .models import Group ,Blog

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields="__all__"

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields="__all__"