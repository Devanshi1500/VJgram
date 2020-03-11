from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html',{'title': ' Shivani '})

def mainpage(request):
    context ={
        'posts':Post.objects.all(),
    }
    return render(request,'mainpage.html',context = context)
