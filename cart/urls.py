from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path('add/<int:product_id>/<int:product_qty>', views.AddProductToCart, name='add_to_cart')
]
