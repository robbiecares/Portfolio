from django.shortcuts import render


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


def tutorials(request):
    template = 'portfolio/tutorials.html'

    context = {
        'title': 'Tutorials'
    }

    return render(request, template, context)

def journal(request):
    template = 'portfolio/journal.html'

    context = {
        'title': 'Journal'
    }

    return render(request, template, context)