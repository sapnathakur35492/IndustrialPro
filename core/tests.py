from django.test import TestCase, Client
from django.urls import reverse
from core.models import SiteSettings

class WebsiteUITests(TestCase):
    def setUp(self):
        self.client = Client()
        SiteSettings.objects.create(company_name="Test Company", email="test@example.com")

    def test_home_page_status(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status(self):
        response = self.client.get(reverse('core:contact_rfq'))
        self.assertEqual(response.status_code, 200)

    def test_rfq_form_submission(self):
        # Test the honeypot field rejecting bots
        data_with_honeypot = {
            'name': 'Bot',
            'company_name': 'Bot Inc',
            'email': 'bot@bot.com',
            'phone': '1234567890',
            'country': 'Botland',
            'product_requirement': 'Parts',
            'message': 'Spam message',
            'honeypot': 'I am a bot'
        }
        response = self.client.post(reverse('core:contact_rfq'), data_with_honeypot)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('honeypot' in response.context['form'].errors)

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User-agent: *")

    def test_sitemap(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
