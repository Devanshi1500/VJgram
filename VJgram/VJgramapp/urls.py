from django.urls import path
from VJgramapp import views

urlpatterns=[
    path('homepage',views.sindex,name='sindex'),
    path('basepage',views.index,name='index'),
]
