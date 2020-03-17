from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView ,DeleteView ,UpdateView
from django.http import HttpResponse, request
from .models import Post
from .forms import PostUpdateForm

'''def home(request):
    context ={
        'posts':Post.objects.all(),
    }
    return render(request,'VJgrampp/mainpage.html',context = context)
'''
#@login_required
class PostListView(ListView,):
    model = Post
    template_name = 'VJgramapp/mainpage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class UserPostListView(ListView):
    model = Post
    template_name = 'VJgramapp/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    #template_name = 'post_form.html'
    #context_object_name = 'posts'
    fields = ['title','content','image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    #template_name = 'post_confirm_delete.html'
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

"""class CommentListVIew(ListView):
    model = Comment

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Comment.objects.filter(user_idr=user).order_by('-date_posted')
"""
def aboutus(request):
    return render(request,'aboutus.html',{'title': ' Shivani '})
