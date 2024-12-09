from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Cart, CartItem
from products.models import Product
from utils.decorators import is_buyer


@login_required(login_url='/buyer/login/')
@is_buyer
def AddProductToCart(request, product_id, product_qty):
    product = get_object_or_404(Product, id=product_id)
    price = product.sales_price * product_qty
    cart, cart_created = Cart.objects.get_or_create(buyer_id=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += product_qty
    cart_item.price += price
    cart_item.save()
    cart.total_price += price
    cart.save()
    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)


@login_required(login_url='/buyer/login/')
@is_buyer
def RemoveProductFromCart(request, product_id, product_qty):
    product = get_object_or_404(Product, id=product_id)
    pass
