from unittest.mock import patch
from django.urls import reverse
from scrappers.models import Rss
from scrappers.tests.scrapper_tastcase import ScrapperTestCase


class RssScrapperTests(ScrapperTestCase):
    def test_it_needs_logged_in_user_in_list(self):
        """
        Test authentication check for index calls
        :return:
        """
        response = self.client.get(reverse('rss.index'))
        self.assertEqual(response.status_code, 302)

    def test_it_needs_logged_in_user_in_details(self):
        """
        Test authentication check for details calls
        :return:
        """
        response = self.client.get(reverse('rss.details', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 302)

    def test_it_displays_the_rss_urls(self):
        """
        Test list display
        :return:
        """
        rss = self.create_rss()
        response = self.client.get(reverse('rss.index'))
        self.assertContains(response, rss.url)

    def test_it_removes_rss(self):
        """
        Test delete records
        :return:
        """
        rss = self.create_rss()
        self.client.delete(reverse('rss.details', kwargs={'id': rss.id}))
        self.assertEquals(0, Rss.objects.count())

    def test_it_adds_new_rss(self):
        """
        Test add requests
        :return:
        """
        self.act_as_user()
        self.client.post(reverse('rss.index'), {'url': 'https://www.nu.nl/rss/Algemeen'})
        self.assertEquals(1, Rss.objects.count())

    def test_scrapper_task_was_called(self):
        """
        Test the task was called automatically after Rss save
        :return:
        """
        with patch('scrappers.tasks.rss_scrapper.delay') as mock_task:
            rss = self.create_rss()
            self.assertTrue(mock_task.called)

    def test_it_displays_rss_contents(self):
        """
        Check content display
        :return:
        """
        rss = self.create_rss()
        response = self.client.get(reverse('rss.details', kwargs={'id': rss.id}))
        self.assertEquals(response.status_code, 200)
