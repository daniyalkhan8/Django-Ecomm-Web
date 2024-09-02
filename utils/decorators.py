from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from functools import wraps
from products.models import Product


# Decorators for sellers

def is_seller(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'seller':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap


def seller_owns_product(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        prod_slug = kwargs.get('prod_slug')

        if not prod_slug:
            return HttpResponseForbidden("Product not specified")
        
        try:
            product = Product.objects.get(slug=prod_slug)
        except Exception:
            return HttpResponseForbidden("Product does not exist")
        
        if product.seller_id != request.user:
            raise PermissionDenied
        
        return view_func(request, *args, **kwargs)
    
    return wrap


# Decorators for buyers

def is_buyer(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'buyer':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap
