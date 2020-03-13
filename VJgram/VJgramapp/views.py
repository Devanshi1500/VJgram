from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView ,DeleteView
from django.http import HttpResponse, request
from .models import Post
from .forms import PostUpdateForm

def home(request):
    return render(request,'home.html')

class PostListView(ListView):
    model = Post
    template_name = 'mainpage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_form.html'
    context_object_name = 'posts'
    fields = ['title','content']

    '''
    po_form = PostUpdateForm(request.POST, request.FILES, instance=request.POST)
    def check():
        if po_form.is_valid():
            po_form.save()
            messages.success(request,f'Your post has been updated.')
            return redirect('post/')
    '''

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_form.html'
    context_object_name = 'posts'
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    #success_url = 'mainpage'

    def test_func(self):
        post = self.get_object
        if self.request.user == post.author:
            return True
        return False

def aboutus(request):
    return render(request,'aboutus.html',{'title': ' Shivani '})

'''def mainpage(request):
    context ={
        'posts':Post.objects.all(),
    }
    return render(request,'mainpage.html',context = context)
'''
