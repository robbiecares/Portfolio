from django.shortcuts import render


def index(request):
    template = 'portfolio/index.html'

    return render(request, template, {})
