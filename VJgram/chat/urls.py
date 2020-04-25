from django.urls import path
from . import views
from .views import MessageListView
from .views import MessageListView ,GroupListView,GroupDetailView,GroupCreateView,GroupUpdateView,GroupDetailView,GroupDeleteView,OthersGroupsListView,UserGroupListView
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('chatpage',MessageListView.as_view(),name='chatpage'),
    path('push',views.inputChat,name="push"),
    path('groups',GroupListView.as_view(),name='groups'),
    path('group/<int:pk>',GroupDetailView.as_view(),name='group-detail'),
    path('group/new/',GroupCreateView.as_view(),name='group-create'),
    path('group/<int:pk>/update/',GroupUpdateView.as_view(),name='group-update'),
    path('group/<int:pk>/delete/',GroupDeleteView.as_view(),name='group-delete'),
    path('othergroups',OthersGroupsListView.as_view(),name='othergroups'),
    path('mycreatedgroups',UserGroupListView.as_view(),name='user-groups'),
    path('joingroup',views.joinGroup,name='joingroup'),
    path('leavegroup', views.leaveGroup, name='leavegroup'),
]
