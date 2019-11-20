from django.db import models
from django.utils import timezone


class GhostPoster(models.Model):
    pick = (True, 'Boast'), (False, 'Roast')
    BoastorRoasts = models.BooleanField(choices=pick)
    post = models.CharField(max_length=280)
    title = models.CharField(max_length=100)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.submission_time}"
