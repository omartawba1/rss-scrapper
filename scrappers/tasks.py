import feedparser
from celery.schedules import crontab
from celery.task import periodic_task
from django.db import transaction, OperationalError
from .models import Rss, Content


@periodic_task(run_every=(crontab(hour='0')), ignore_result=True, retries=5, autoretry_for=(OperationalError,))
def rss_scrapper(rss_id):
    """
    Task to crawl rss url and save the content to the db
    :param rss_id:
    """
    rss = Rss.objects.get(pk=rss_id)
    with transaction.atomic():
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
    return True
