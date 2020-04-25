from django.contrib import admin
from .models import Message,Group,GroupMember

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(GroupMember)



# Register your models here.
