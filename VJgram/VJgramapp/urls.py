from django.urls import path
from VJgramapp import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('mainpage',views.mainpage,name='mainpage')
]
