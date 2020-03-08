from django.shortcuts import render
from django.urls import reverse_lazy

from . import forms

class SignUp(CreateView):
    form_Class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'VJgramapp/home.html' 
