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
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
