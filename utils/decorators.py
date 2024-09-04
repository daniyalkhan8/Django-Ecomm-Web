from django.core.exceptions import PermissionDenied
from functools import wraps


# Decorators for sellers

def is_seller(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'seller':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap


# Decorators for buyers

def is_buyer(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == 'buyer':
            return view_func(request, *args, **kwargs)
        raise PermissionDenied
    return wrap
