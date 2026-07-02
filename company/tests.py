from django.test import TestCase, Client
from django.urls import reverse

class CompanyTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_capabilities_page(self):
        response = self.client.get(reverse('company:capabilities'))
        self.assertEqual(response.status_code, 200)

    def test_infrastructure_page(self):
        response = self.client.get(reverse('company:infrastructure'))
        self.assertEqual(response.status_code, 200)

    def test_certifications_page(self):
        response = self.client.get(reverse('company:certifications'))
        self.assertEqual(response.status_code, 200)

    def test_export_markets_page(self):
        response = self.client.get(reverse('company:export_markets'))
        self.assertEqual(response.status_code, 200)
