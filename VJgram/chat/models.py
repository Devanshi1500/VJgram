from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    creator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="creator")
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    icon = models.ImageField(default='vjti.jpg',upload_to='media/post_pics')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.group_id)

    def get_absolute_url(self):
        return reverse('group-detail',kwargs={'pk':self.pk})

class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    user_id_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userfrom")
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="groupname",default=1)

    def __str__(self):
        return str(self.message_id)

class GroupMember(models.Model):
    gpm_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(User,on_delete=models.CASCADE,related_name="member")
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name="group",default=1)

    def __str__(self):
        return str(self.gpm_id)
