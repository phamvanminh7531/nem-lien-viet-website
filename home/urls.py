from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('san-pham/<str:slug>/', product_detail, name="product"),
    path('san-pham-theo-danh-muc/<str:slug>/', product_list_by_category, name="product_list_by_category"),
    path('tat-ca-san-pham/', all_products, name="all_products"),
]