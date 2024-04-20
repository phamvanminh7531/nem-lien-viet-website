from django.db import models
from django.template.defaultfilters import slugify
import unidecode

def vi_slug(data):
    vietnamese_map = {
        ord(u'o'): 'o', ord(u'ò'): 'o', ord(u'ó'): 'o', ord(u'ỏ'): 'o', ord(u'õ'): 'o', ord(u'ọ'): 'o',
        ord(u'ơ'): 'o', ord(u'ờ'): 'o', ord(u'ớ'): 'o', ord(u'ở'): 'o', ord(u'ỡ'): 'o', ord(u'ợ'): 'o',
        ord(u'ô'): 'o', ord(u'ồ'): 'o', ord(u'ố'): 'o', ord(u'ổ'): 'o', ord(u'ỗ'): 'o', ord(u'ộ'): 'o',

        ord(u'à'): 'a', ord(u'á'): 'a', ord(u'á'): 'a', ord(u'ả'): 'a', ord(u'ã'): 'a', ord(u'ạ'): 'a',
        ord(u'ă'): 'a', ord(u'ắ'): 'a', ord(u'ằ'): 'a', ord(u'ẳ'): 'a', ord(u'ẵ'): 'a', ord(u'ạ'): 'a',
        ord(u'â'): 'a', ord(u'ầ'): 'a', ord(u'ấ'): 'a', ord(u'ậ'): 'a', ord(u'ẫ'): 'a', ord(u'ẩ'): 'a',

        ord(u'đ'): 'd', ord(u'Đ'): 'd',

        ord(u'è'): 'e', ord(u'é'): 'e', ord(u'ẻ'): 'e', ord(u'ẽ'): 'e', ord(u'ẹ'): 'e',
        ord(u'ê'): 'e', ord(u'ề'): 'e', ord(u'ế'): 'e', ord(u'ể'): 'e', ord(u'ễ'): 'e', ord(u'ệ'): 'e',

        ord(u'ì'): 'i', ord(u'í'): 'i', ord(u'ỉ'): 'i', ord(u'ĩ'): 'i', ord(u'ị'): 'i',
        ord(u'ư'): 'u', ord(u'ừ'): 'u', ord(u'ứ'): 'u', ord(u'ử'): 'ữ', ord(u'ữ'): 'u', ord(u'ự'): 'u',
        ord(u'ý'): 'y', ord(u'ỳ'): 'y', ord(u'ỷ'): 'y', ord(u'ỹ'): 'y', ord(u'ỵ'): 'y',
    }
    slug = slugify(str(data).translate(vietnamese_map))
    return slug

def upload_path(instance, filename):
    name = unidecode.unidecode(instance.product_name).replace(" ", "-").lower()
    return 'images/{0}'.format(name)

def upload_path_carousel(instance, filename):
    name = unidecode.unidecode(instance.carousel_name).replace(" ", "-").lower()
    return 'images/{0}'.format(name)




# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=250, unique=True, verbose_name="Tên Danh Mục")
    slug  = models.SlugField(blank=True)

    def __str__(self) -> str:
        return self.category_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = vi_slug(self.category_name)
        super(ProductCategory, self).save(*args, **kwargs)

class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name="Tên Sản Phẩm")
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name="Danh Mục Sản Phẩm")
    description = models.TextField(verbose_name="Miêu Tả Sản Phẩm")
    price = models.BigIntegerField(blank=True, verbose_name="Giá Cũ")
    fix_price = models.BigIntegerField(blank=True, verbose_name="Giá Khuyến Mãi")
    images = models.FileField(upload_to = upload_path, verbose_name="Ảnh")
    slug  = models.SlugField(blank=True)

    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = vi_slug(self.product_name)
        super(Product, self).save(*args, **kwargs)

class BaseInfo(models.Model):
    phone_num_1 = models.CharField(max_length=12, blank=True , verbose_name="Số Điện Thoại 1")
    phone_num_2 = models.CharField(max_length=12, blank=True , verbose_name="Số Điện Thoại 2")
    address = models.CharField(max_length=255, unique=True, verbose_name="Địa Chỉ")

    def __str__(self) -> str:
        return super().__str__()

class CarouselImage(models.Model):
    carousel_name = models.CharField(max_length=250, unique=True, verbose_name="Tên Ảnh")
    images = models.FileField(upload_to = upload_path_carousel, verbose_name="Ảnh")

    def __str__(self) -> str:
        return self.carousel_name