from django.contrib import admin
from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('resource/', views.ResourceListView.as_view(), name='resources'),
    path('resources/<int:pk>', views.ResourceDetailView.as_view(), name='resource-detail'),

]
