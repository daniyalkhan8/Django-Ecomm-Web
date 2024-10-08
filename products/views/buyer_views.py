from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.core.paginator import Paginator

from ..models import Product, Category


def BuyerProductList(request):
    if request.method == "GET":
        product_search = request.GET.get('product_search')
        category_search = request.GET.get('category_search')
        product_list = Product.objects.all().order_by('-created_at')

        if product_search:
            product_list = product_list.filter(name__icontains=product_search)

        if category_search:
            product_list = product_list.filter(category__id=int(category_search))

        categories = Category.objects.all()
        paginator = Paginator(product_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(
        request, 
        'products/buyer/product_list.html', 
        {'page_obj': page_obj, 'categories': categories, 'product_search': product_search}
    )


def BuyerViewProduct(request, prod_slug):
    if request.method == "GET":
        try:
            product = get_object_or_404(
                Product, 
                slug=prod_slug
            )
        except Exception:
            return HttpResponseNotFound("Product Not Found.")
        
        images = product.images.all()

        return render(
            request,
            'products/buyer/product_view.html',
            {'product': product, 'images': images}
        )
