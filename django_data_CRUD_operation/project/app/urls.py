from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="home"),
    path('registered',views.success,name="success"),
    path('insert',views.insert,name="insert"),
    path('show',views.show,name="show"),
    path("edit<int:id>", views.edit, name="edit"),
    path("update<int:id>", views.update, name="update"),
    path("delete<int:id>", views.destroy, name="delete"),
]