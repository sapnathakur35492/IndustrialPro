from django.test import TestCase, Client
from django.urls import reverse
from catalog.models import Category, Product

class CatalogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Castings", slug="castings")
        self.product = Product.objects.create(name="Steel Valve", slug="steel-valve", category=self.category, description="Test description")

    def test_product_list(self):
        response = self.client.get(reverse('catalog:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Steel Valve")

    def test_product_detail(self):
        response = self.client.get(reverse('catalog:product_detail', args=[self.product.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Steel Valve")

    def test_industry_list(self):
        response = self.client.get(reverse('catalog:industry_list'))
        self.assertEqual(response.status_code, 200)
