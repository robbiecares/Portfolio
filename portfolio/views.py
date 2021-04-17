from django.shortcuts import render
from django.views import generic

from portfolio.models import Resource, Project


def index(request):
    template = 'portfolio/index.html'

    context = {
        'title': 'Home'
    }

    return render(request, template, context)


def about(request):
    template = 'portfolio/about.html'

    context = {
        'title': 'About',
        'description': 'This site was created by robbiecares@gmail.com. It will be used to showcase projects he '
                       'develops and to document his progress as he self-studies to become a software developer.'
    }

    return render(request, template, context)


# def projects(request):
#     template = 'portfolio/projects.html'
#
#     context = {
#         'title': 'Projects'
#     }
#
#     return render(request, template, context)


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


class ProjectDetailView(generic.DetailView):
    model = Project


class ProjectListView(generic.ListView):
    model = Project

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Projects'
        return context
