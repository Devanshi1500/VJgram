from django.views.generic import TemplateView
from django.shortcuts import render
class HomePage(TemplateView):
    template_name ='home.html'

