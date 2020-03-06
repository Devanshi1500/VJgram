from django.urls import path
from VJgramapp import views

urlpatterns=[
    path('',views.sindex,name='sindex')
]
