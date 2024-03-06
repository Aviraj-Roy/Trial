from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('registered',views.success,name="success"),
    path('insert',views.insert,name="insert")
]