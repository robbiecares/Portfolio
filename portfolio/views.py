from django.shortcuts import render
from django.views import generic

from portfolio.models import Resource


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


class ResourceDetailView(generic.DetailView):
    model = Resource


class ResourceListView(generic.ListView):
    model = Resource

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(ResourceListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Resources'
        return context
