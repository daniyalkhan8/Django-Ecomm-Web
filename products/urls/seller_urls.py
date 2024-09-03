from django.urls import path
from .. import views


app_name = "seller_products"
urlpatterns = [
    path('add-product/', views.SellerAddProduct, name='add_product'),
    path('product-list/', views.SellerProductList, name='product_list'),
    path('update-product/<slug:prod_slug>', views.SellerUpdateProduct, name='update_product'),
    path('delete-product/<slug:prod_slug>', views.SellerDeleteProduct, name='delete_product'),
]
