from django.contrib.auth.models import User
from django.urls import reverse
from scrappers.tests.scrapper_tastcase import ScrapperTestCase
from scrappers.models import Content


class FavouritesTests(ScrapperTestCase):
    def test_it_needs_logged_in_user_in_list(self):
        """
        Test authentication gateway
        :return:
        """
        response = self.client.get(reverse('favourites.index'))
        self.assertEqual(response.status_code, 302)

    def test_it_shows_favourite_items_favourites_list(self):
        """
        Test it shows the correct favourite items in the list
        :return:
        """
        rss = self.create_rss()
        favourite_content = Content(title='test1', content='content1', rss=rss, favourite=True)
        favourite_content.save()
        response = self.client.get(reverse('favourites.index'))
        self.assertContains(response, favourite_content.title)

    def test_it_does_not_show_not_favourite_items_in_favourites_list(self):
        """
        Test not showing normal items in the favourites list
        :return:
        """
        rss = self.create_rss()
        normal_content = Content(title='test2', content='content1', rss=rss, favourite=False)
        normal_content.save()
        response = self.client.get(reverse('favourites.index'))
        self.assertNotContains(response, normal_content.title)

    def test_it_adds_favourite_item(self):
        """
        Test adding favourite to my list
        :return:
        """
        rss = self.create_rss()
        content = Content(title='test2', content='content1', rss=rss, favourite=False)
        content.save()
        self.client.post(reverse('favourites.details', kwargs={'id': content.id}))
        self.assertEquals(Content.favourites.filter(rss__user=User.objects.first()).count(), 1)

    def test_it_removes_favourite_item(self):
        """
        Test remove favourite from the list
        :return:
        """
        rss = self.create_rss()
        content = Content(title='test2', content='content1', rss=rss, favourite=True)
        content.save()
        self.client.delete(reverse('favourites.details', kwargs={'id': content.id}))
        self.assertEquals(Content.favourites.filter(rss__user=User.objects.first()).count(), 0)
