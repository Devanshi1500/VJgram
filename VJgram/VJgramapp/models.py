from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
#class User(auth.models.User,auth.models.PermissionsMixin):

#    def __str__(self):
#        return "@{}".format(self.username)

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
