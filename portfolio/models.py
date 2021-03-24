from django.db import models
from django.urls import reverse


class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    units = models.IntegerField(default=1)
    url = models.URLField(blank=True)

    tutorial_statuses = [
        ('s', 'started'),
        ('a', 'active'),
        ('c', 'completed'),
    ]

    status = models.CharField(max_length=1, choices=tutorial_statuses, default='s')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:tutorial-detail', args=[str(self.id)])

    class Meta:
        ordering = ['name']