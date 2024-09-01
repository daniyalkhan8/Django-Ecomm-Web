from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, ProductImages, Category
from .forms import ProductCreatForm, ProductUpdateForm
from utils.decorators import is_seller


# Seller Products Views

@login_required(login_url="/seller/login/")
@is_seller
def SellerAddProduct(request):
    if request.method == "POST":
        product_form = ProductCreatForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller_id = request.user
            product.save()
            images = request.FILES.getlist('product_images')
            for image in images:
                product_image = ProductImages.objects.create(image=image)
                product.images.add(product_image)
            return redirect('sellers:product_seller:product_list')
    else:
        product_form = ProductCreatForm()
        
    return render(
        request, 
        "products/seller/add_product.html", 
        {"form": product_form}
    )


@login_required(login_url='/seller/login/')
@is_seller
def SellerUpdateProduct(request, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug)

    if request.method == "POST":
        pass
    else:
        product_form = ProductUpdateForm(instance=product)

    return render(
        request, 
        'products/seller/update_product.html',
        {'form': product_form, 'product': product}
    )


@login_required(login_url="/seller/login/")
@is_seller
def SellerProductList(request):
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
        'products/seller/product_list.html', 
        {'page_obj': page_obj, 'categories': categories}
    )
