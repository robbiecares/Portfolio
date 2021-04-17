from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from portfolio.models import Activity


class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # todo: what should happen if a user is removed from the system? Set author value to 'deleted' (like Reddit)?
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('journal:entry-detail', kwargs={'pk': self.pk})



