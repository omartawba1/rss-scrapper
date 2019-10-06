from django.contrib.auth.models import User
from django.test import TestCase

from scrappers.models import Rss


class ScrapperTestCase(TestCase):
    def act_as_user(self):
        """
        Make the requests within logged-in user
        :return User:
        """
        user = User.objects.create_user('john', 'john@doe.com', '123')
        self.client.login(username='john', password='123')
        return user

    def create_rss(self):
        """
        Create rss for testing purposes
        :return Rss:
        """
        user = self.act_as_user()
        rss = Rss()
        rss.url = 'https://www.nu.nl/rss/Algemeen'
        rss.user = user
        rss.save()
        return rss
