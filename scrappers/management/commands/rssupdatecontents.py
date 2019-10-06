import feedparser
from django.core.management.base import BaseCommand
from django.db import transaction

from scrappers.models import Rss, Content


class Command(BaseCommand):
    help = 'Update the content for the rss records'

    def handle(self, *args, **options):
        with transaction.atomic():
            for rss in Rss.objects.all():
                Content.objects.filter(rss=rss, favourite=False).delete()
                feed = feedparser.parse(rss.url)
                for i in range(0, len(feed['entries'])):
                    if feed['entries'][i]:
                        rss_content = Content()
                        rss_content.rss = rss
                        rss_content.title = feed['entries'][i].title
                        rss_content.content = feed['entries'][i].description
                        rss_content.favourite = False
                        rss_content.save()

        self.stdout.write(self.style.SUCCESS('Successfully rss content updated'))
