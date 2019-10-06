from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class HomepageTests(TestCase):
    def setUp(self):
        self.__response = self.client.get(reverse('homepage'))

    def test_homepage_page_landing(self):
        """
        Basic test for health check
        :return:
        """
        self.assertEqual(self.__response.status_code, 200)

    def test_it_uses_the_correct_template(self):
        """
        Check that the homepage uses the correct template
        :return:
        """
        self.assertTemplateUsed(self.__response, 'homepage/index.html')

    def test_it_show_auth_buttons_while_guest_user(self):
        """
        It displays the authentication buttons with guest users
        :return:
        """
        self.assertContains(self.__response, 'Signup')

    def test_it_shows_rss_buttons_while_logged_in_user(self):
        """
        It displays the application buttons with the logged in users
        :return:
        """
        user = User.objects.create_user('john', 'john@doe.com', '123')
        self.client.login(username='john', password='123')
        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'Rss Data')
