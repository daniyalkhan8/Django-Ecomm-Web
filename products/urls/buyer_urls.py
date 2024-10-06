from django.urls import path
from ..views import buyer_views


app_name = "buyer_products"
urlpatterns = [
    path('product-list/', buyer_views.BuyerProductList, name='product_list'),
    path('product/<slug:prod_slug>', buyer_views.BuyerViewProduct, name='product_view'),
]
