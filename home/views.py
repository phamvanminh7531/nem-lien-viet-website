from django.shortcuts import render
from .models import ProductCategory, Product, BaseInfo

# Create your views here.


def home(request):
    products = Product.objects.all()[:9]
    context = {
        'products_1' : products[:4],
        'products_2' : products[4:9],
    }
    
    return render(request, "home/home.html", context=context)

def product_detail(request, slug):
    product_categories = ProductCategory.objects.all()
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.all()[:4]
    context = {
        'categories':product_categories,
        'product':product,
        'related_products':related_products
    }

    return render(request, 'home/product_detail.html', context=context)

def product_list_by_category(request, slug):
    product_category = ProductCategory.objects.get(slug = slug)
    products = Product.objects.filter(category = product_category)
    
    product_list = []
    """
    Split product list to list len = 4
    """
    start = 0
    end = len(products)
    STEP = 4
    for i in range(start, end, STEP):
        x = i
        product_list.append(products[x:x+STEP])
    
    context = {
        'product_list':product_list
    }

    return render(request, "home/product_shop.html", context=context)

def all_products(request):
    product_list = []
    products = Product.objects.all()
    """
    Split product list to list len = 4
    """
    start = 0
    end = len(products)
    STEP = 4
    for i in range(start, end, STEP):
        x = i
        product_list.append(products[x:x+STEP])
    
    context = {
        'product_list':product_list
    }

    return render(request, "home/product_shop.html", context=context)