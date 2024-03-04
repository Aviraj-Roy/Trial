from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('second',views.secondPage,name="page2"),
]