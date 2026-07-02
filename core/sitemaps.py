from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from catalog.models import Category, Product, Industry

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['core:home', 'core:about', 'core:contact_rfq', 'company:capabilities', 'company:infrastructure', 'company:certifications', 'company:export_markets', 'catalog:product_list', 'catalog:industry_list']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return Product.objects.all()

    def location(self, item):
        return reverse('catalog:product_detail', args=[item.slug])
