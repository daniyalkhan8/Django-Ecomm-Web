from django.urls import path
from ..views import seller_views


app_name = "seller_products"
urlpatterns = [
    path('add-product/', seller_views.SellerAddProduct, name='add_product'),
    path('product-list/', seller_views.SellerProductList, name='product_list'),
    path('update-product/<slug:prod_slug>', seller_views.SellerUpdateProduct, name='update_product'),
    path('delete-product/<slug:prod_slug>', seller_views.SellerDeleteProduct, name='delete_product'),
]
