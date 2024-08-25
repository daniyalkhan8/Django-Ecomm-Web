from django.urls import path
from .. import views


app_name = "seller_products"
urlpatterns = [
    path('add-product', views.SellerAddProduct, name='add_product'),
]
