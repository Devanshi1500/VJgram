from django.urls import path
from.views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDetailView,PostDeleteView
from VJgramapp import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('mainpage/',PostListView.as_view(),name='mainpage'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),

]

#<app>/<model>_<viewtype>.html
