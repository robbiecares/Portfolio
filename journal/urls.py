"""blog_app URL Configuration"""

from django.urls import path
from .views import (
    EntryListView,
    EntryDetailView,
    EntryCreateView,
    EntryUpdateView,
    EntryDeleteView,
    UserEntryListView,
)
from . import views

app_name = 'journal'

urlpatterns = [
    path('', EntryListView.as_view(), name='home'),
    path('user/<str:username>', UserEntryListView.as_view(), name='user-entries'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
    path('entry/new/', EntryCreateView.as_view(), name='entry-create'),
    path('entry/<int:pk>/update/', EntryUpdateView.as_view(), name='entry-update'),
    path('entry/<int:pk>/delete/', EntryDeleteView.as_view(), name='entry-delete'),
    path('about/', views.about, name='about'),

]

