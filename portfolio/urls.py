from django.contrib import admin
from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tutorials/', views.TutorialListView.as_view(), name='tutorials'),
    path('tutorials/<int:pk>', views.TutorialDetailView.as_view(), name='tutorial-detail'),
    # path('journal/', views.journal, name='portfolio-journal'),

]
