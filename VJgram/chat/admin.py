from django.contrib import admin
from .models import Message,MessageTo,Group,GroupMember

admin.site.register(Group)
admin.site.register(Message)
admin.site.register(GroupMember)
admin.site.register(MessageTo)


# Register your models here.
