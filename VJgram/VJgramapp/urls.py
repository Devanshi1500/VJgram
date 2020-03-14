from django.urls import path
from.views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDetailView,PostDeleteView,UserPostListView
from VJgramapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #path('home/',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('home/',PostListView.as_view(),name='home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
     path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#<app>/<model>_<viewtype>.html
