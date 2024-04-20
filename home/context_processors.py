from home.models import BaseInfo, ProductCategory, CarouselImage

def load_base_info(request):
    categories = ProductCategory.objects.all()
    info = BaseInfo.objects.all()[0]
    return {'info': info, 'categories': categories}

def load_carousel_imge(request):
    carousel_images = CarouselImage.objects.all()
    return {'carousel_images':carousel_images[1::], 'active_image':carousel_images[0]}