from django.db import models
from django.db.models import Manager
from scrappers.models.rss import Rss


class FavouritesManager(models.Manager):
    def get_queryset(self):
        return super(FavouritesManager, self).get_queryset().filter(favourite=True)


class Content(models.Model):
    """
    Here you can find the scrappers content
    """
    rss = models.ForeignKey(Rss, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    favourite = models.BooleanField(default=False)
    favourites = FavouritesManager()
    objects = Manager()

    class Meta:
        ordering = ['-favourite']

    def __str__(self):
        return self.title
