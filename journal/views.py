from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Entry


# def home(request):
#     template = 'journal/index.html'
#     context = {
#         'entries': Entry.objects.all(),
#     }
#
#     return render(request, template, context)


class EntryListView(ListView):
    model = Entry
    template_name = 'journal/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'entries'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Journal'
        return context


class UserEntryListView(ListView):
    model = Entry
    template_name = 'journal/user_entries.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'entries'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Entry.objects.filter(author=user).order_by('-date_posted')


class EntryDetailView(DetailView):
    model = Entry


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'journal/entry_form.html'
    context_object_name = 'entry'
    fields = ['title', 'activity', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    fields = ['title', 'activity', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        entry = self.get_object()
        return True if self.request.user == entry.author else False


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = '/'

    def test_func(self):
        entry = self.get_object()
        if self.request.user == entry.author:
            return True
        return False


def about(request):
    template = 'journal/about.html'
    context = {}

    return render(request, template, context)

