from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView ,DeleteView ,UpdateView
from django.http import HttpResponse, request,JsonResponse
from .models import Message,GroupMember,Group,MessageTo
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


class GroupListView(ListView,):
    model = Group
    template_name = 'chat/groups.html'
    context_object_name = 'groups'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        user = self.request.user
        g = [groupmember.group for groupmember in GroupMember.objects.filter(member=user)]
        context['g'] = g
        return context

class GroupCreateView(CreateView):
    model = Group
    fields = ['title','icon','description']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class GroupUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Group
    fields = ['title','icon','description']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def test_func(self):
        group = self.get_object()
        if self.request.user == group.creator:
            return True
        return False

class GroupDetailView(DetailView):
    model = Group
    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        user = self.request.user
        messages = [message for message in Message.objects.filter(group=self.object)]
        members = [member.member for member in GroupMember.objects.filter(group=self.object)]
        mt=[user.username for user in members]
        context['chats'] = messages
        context['members'] = mt
        # And so on for more models
        return context


class GroupDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Group
    #template_name = 'post_confirm_delete.html'
    success_url = '/othergroups'

    def test_func(self):
        group = self.get_object()
        if self.request.user == group.creator:
            return True
        return False

class UserGroupListView(ListView):
    model = Group
    template_name = 'chat/user_groups.html'
    context_object_name = 'groups'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Group.objects.filter(creator=user).order_by('-date_created')

class OthersGroupsListView(ListView):
    model = Group
    template_name = 'chat/othergroups.html'
    context_object_name = 'othergroups'

    def get_context_data(self, **kwargs):
        context = super(OthersGroupsListView, self).get_context_data(**kwargs)
        user = self.request.user
        mygroups = [user.group for user in GroupMember.objects.filter(member=user)]
        othergroups=[]
        for group in Group.objects.all():
            if group in mygroups:
                continue;
            else:
                othergroups.append(group)
        context['othergroups'] = othergroups
        return context

@csrf_exempt
def joinGroup(request):
        if request.method == 'POST':
               group_id = request.POST['group_id']
               user = request.user
               group = Group.objects.get(group_id=group_id)
               m = GroupMember(member=user,group=group) # Creating GroupMember Object
               m.save()
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")

@csrf_exempt
def leaveGroup (request):
        if request.method == 'POST':
               group_id = request.POST['group_id']
               user = request.user
               GroupMember.objects.get(group_id=group_id,member=user).delete()# Deleting GroupMember Object
               return HttpResponse("Success!")
        else:
               return HttpResponse("Request method is not a GET")

@csrf_exempt
def inputChat(request):
        if request.method == 'POST':
            group_id = request.POST['group_id']
            userd = request.user
            queryset = userd.username
            content = request.POST.get('content',False)
            group = Group.objects.get(group_id=group_id)
            m = Message(user_id_from=userd,content=content,group=group) # Creating Message Object
            m.save()
            return JsonResponse({'user_id':queryset,'content':content}) # Sending an success response
        else:
            return HttpResponse("Request method is not a GET")



class MessageListView(ListView):
    model = Message
    template_name = 'chat/chathome.html'
    context_object_name = 'chats'
    ordering = ['date_created']
