from django.test import TestCase

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') 
        self.assertContains(response, "<tile>To-Do lists</title>")
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")
