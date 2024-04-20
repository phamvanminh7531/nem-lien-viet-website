from django.contrib import admin
from .models import ProductCategory, Product, BaseInfo, CarouselImage
from django.utils.html import format_html

# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']

    class Meta:
        model = ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'category', 'description', 'price', 'fix_price', 'images', 'image_tag']
    readonly_fields = ['image_tag']


    class Meta:
        model = Product
    
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.images.url))

@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    fields = ['carousel_name', 'images', 'image_tag']
    readonly_fields = ['image_tag']

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.images.url))

admin.site.register(BaseInfo)