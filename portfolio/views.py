from django.shortcuts import render
from django.views import generic

from .models import Resource, Project, Activity
from journal.models import Entry


def index(request):
    template = 'portfolio/index.html'
    projects = Project.objects.filter(status='c')
    entries = Entry.objects.all().order_by('-date_posted')[:3]
    resources = Resource.objects.filter(status='a')
    context = {
        'title': 'Home',
        'projects': projects,
        'entries': entries,
        'resources': resources,
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

def gallery(request):
    template = 'portfolio/gallery.html'

    context = {
        'title': 'Gallery',
    }

    return render(request, template, context)

class ActivityDetailView(generic.DetailView):
    model = Activity
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['entries'] = self.object.entry_set.all().order_by('-date_posted')
        return context


class ProjectListView(generic.ListView):
    model = Project

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(ProjectListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Projects'
        return context


class ProjectDetailView(generic.DetailView):
    model = Project

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['entries'] = self.object.entry_set.all()
        return context


class ResourceListView(generic.ListView):
    model = Resource
    template_name = 'portfolio/education.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        # Call the base implementation first to get the context
        context = super(ResourceListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['title'] = 'Education'
        return context




