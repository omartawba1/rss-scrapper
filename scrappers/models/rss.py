from django.db import models
from django.contrib.auth.models import User


class Rss(models.Model):
    """
    Here is the scrappers RSS model
    """
    url = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
