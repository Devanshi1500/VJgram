from django.urls import path
from . import views
from .views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDetailView,PostDeleteView,UserPostListView,FriendListView,OthersUsersListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path(r'^$',views.home),
    path('mainpage/',PostListView.as_view(),name='mainpage'),
    path('home/',views.home,name='home1'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('myposts',UserPostListView.as_view(),name='user-posts'),
    path('commentPost',views.commentPost,name='commentPost'),
    path('likepost', views.likePost, name='likepost'),
    path('removefriend', views.removeFriend, name='removefriend'),
    path('addfriend', views.addFriend, name='addfriend'),
    path('mainpage/friends/<str:username>',FriendListView.as_view(),name='friends'),
    path('otherusers',OthersUsersListView.as_view(),name='otherusers'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#<app>/<model>_<viewtype>.html
