from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='vjti.jpg',upload_to='profile_pics')
    GENDER = (('M','Male'),('F','Female'),('O','Other'))
    gender = models.CharField(default='O',max_length=1,choices=GENDER)
    birth_date = models.DateField(default=timezone.now)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
