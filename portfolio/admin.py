from django.contrib import admin

from portfolio.models import Project, Resource, Competency


admin.site.register(Competency)
admin.site.register(Project)
admin.site.register(Resource)
