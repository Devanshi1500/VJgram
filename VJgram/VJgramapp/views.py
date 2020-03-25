from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView ,DeleteView ,UpdateView
from django.http import HttpResponse, request
from .models import Post,Comment,Like
from .forms import PostUpdateForm,CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

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

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['comments'] = Comment.objects.all()
        context['likes'] = Like.objects.all()
        # And so on for more models
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'VJgramapp/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        postid = get_object_or_404(Post,id=self.kwargs.get('pk'))
        context['comments'] = Comment.objects.filter(post_id=postid)
        context['likes'] = Like.objects.filter(post_id=postid)
        # And so on for more models
        return context

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

#class CommentListView(ListView):
#    model = Comment
#    context_object_name = 'comments'
#    template_name = 'VJgramapp/mainpage.html'


 #   def get_queryset(self):
        #user = get_object_or_404(Post,id=self.kwargs.get('post_id'))
 #       return Comment.objects.all()
@csrf_exempt
def likePost(request):
        if request.method == 'POST':
               post_id = request.POST['post_id']
               user_id = request.user
               likedpost = Post.objects.get(pk=post_id) #getting the liked posts
               m = Like(post_id=likedpost,user_id=user_id,l=True) # Creating Like Object
               m.save()  # saving it to store in database
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")

@csrf_exempt
def commentPost(request):
        if request.method == 'POST':
            post_id = request.POST['post_id']
            user_id = request.user
            comment = request.POST.get('content',False)
            likedpost = Post.objects.get(pk=post_id) #getting the liked posts
            m = Comment(post_id=likedpost,user_id=user_id,content=comment) # Creating Like Object
            m.save()
            return HttpResponse("Success!") # Sending an success response

        else:

            return HttpResponse("Request method is not a GET")

def aboutus(request):
    return render(request,'aboutus.html',{'title': ' Shivani '})

def createcomment(request):
    return 0
