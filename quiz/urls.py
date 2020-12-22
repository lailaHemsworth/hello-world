from django.urls import path
from . import views

urlpatterns = [
    path('', views.create , name = "create.html"),
    path('add', views.addQuestion , name = "add"),
    
]
