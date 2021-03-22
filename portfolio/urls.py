from django.contrib import admin
from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('journal/', views.journal, name='journal'),

]
