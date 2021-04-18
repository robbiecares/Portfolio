# from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse


class Activity(models.Model):
    """A class to represent the details of my daily coding activities."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    statuses = [
        ('a', 'active'),
        ('i', 'inactive'),
        ('c', 'completed'),
    ]
    status = models.CharField(max_length=1, choices=statuses, default='i')
    start_date = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True)
    repository = models.URLField(blank=True)
    # entries = GenericRelation(Entry)

    def __str__(self):
        return self.name

    # class Meta:
    #     ordering = ['name']


class Project(Activity):
    """Represents the details of projects I create."""
    # todo: plan - a list of the steps I've outlined to complete the project
    # todo: status - I could include a "idea" status as by subclassing statuses
    pass

    def get_absolute_url(self):
        return reverse('portfolio:project-detail', args=[str(self.id)])


class Resource(Activity):
    """Represents the details of resources I use for learning."""
    types = [
        ('b', 'book'),
        ('e', 'exercises'),
        ('t', 'tutorial'),
    ]
    type = models.CharField(max_length=1, choices=types)

    def get_absolute_url(self):
        return reverse('portfolio:resource-detail', args=[str(self.id)])
