from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rss
from scrappers.tasks import rss_scrapper


@receiver(post_save, sender=Rss)
def new_rss_added(sender, instance, **kwargs):
    """
    Signal for dispatching the scrapper task after a new rss addition
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    rss_scrapper.delay(instance.id)
