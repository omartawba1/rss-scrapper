from django.apps import AppConfig


class ScrapperConfig(AppConfig):
    name = 'scrappers'

    def ready(self):
        import scrappers.signals
