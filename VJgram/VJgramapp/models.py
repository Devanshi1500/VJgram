from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#class User(auth.models.User,auth.models.PermissionsMixin):

#    def __str__(self):
#        return "@{}".format(self.username)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default='vjti.jpg',upload_to='media/post_pics')

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Friend(models.Model):
    friend_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user",default=1)
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name="following",default=1)

    def __str__(self):
        return str(self.friend_id)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.comment_id)

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    l = models.BooleanField()
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.like_id)
