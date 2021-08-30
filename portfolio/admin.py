from django.contrib import admin
from portfolio.models import Project, Resource, Language, Competency


admin.site.register(Competency)
admin.site.register(Language)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_competencies', 'display_languages')


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_competencies', 'display_languages')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Resource, ResourceAdmin)




