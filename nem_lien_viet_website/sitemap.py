from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from home.models import Product, ProductCategory
from datetime import datetime

class ProductSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return Product.objects.all()
    
    def lastmod(self, obj):
        return datetime(2024, 4, 21)
    
    def location(self, obj):
        return '/san-pham/%s' % (obj.slug)

class ProductCategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'
 
    def items(self):
        return ProductCategory.objects.all()
    
    def lastmod(self, obj):
        return datetime(2024, 4, 21)
    
    def location(self, obj):
        return '/san-pham-theo-danh-muc/%s' % (obj.slug)

class MainSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return [
            '',
            '/home',
            '/tat-ca-san-pham'
            ]

    # def lastmod(self, obj):
    #     return obj.lastEdit_date
    def lastmod(self, item):
        return datetime(2024, 4, 21)

    def location(self, obj):
        return obj

