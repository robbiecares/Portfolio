from django.shortcuts import render
from django.views import generic

from portfolio.models import Tutorial


def index(request):
    template = 'portfolio/index.html'

    context = {
        'title': 'Home'
    }

    return render(request, template, context)


def about(request):
    template = 'portfolio/about.html'

    context = {
        'title': 'About'
    }

    return render(request, template, context)


def projects(request):
    template = 'portfolio/projects.html'

    context = {
        'title': 'Projects'
    }

    return render(request, template, context)


class TutorialDetailView(generic.DetailView):
    model = Tutorial


class TutorialListView(generic.ListView):
    model = Tutorial

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(TutorialListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Tutorials'
        return context


def journal(request):
    template = 'portfolio/journal.html'

    context = {
        'title': 'Journal'
    }

    return render(request, template, context)