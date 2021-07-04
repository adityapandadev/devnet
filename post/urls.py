from django.contrib import admin
from django.urls import path
from .views import HomeView, PostCreateView 
from post import views


urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('add_post/', PostCreateView.as_view(), name = "add_post"),
]
