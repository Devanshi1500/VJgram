from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post,Comment

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"

class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post_id','content']
