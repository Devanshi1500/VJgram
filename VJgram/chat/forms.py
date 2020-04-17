from django.contrib.auth import get_user_model
from django import forms
from .models import Group

class GroupUpdateForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['title','icon','description']
