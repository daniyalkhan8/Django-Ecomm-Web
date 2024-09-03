from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.urls import reverse

from .models import Product, ProductImages, Category
from .forms import ProductForm
from utils.decorators import is_seller


# Seller Products Views

@login_required(login_url="/seller/login/")
@is_seller
def SellerAddProduct(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.seller_id = request.user
            product.save(commit=False)
            images = request.FILES.getlist('product_images')

            for image in images:
                product_image = ProductImages.objects.create(image=image)
                product.images.add(product_image)

            product.save()
            return redirect('sellers:product_seller:product_list')
    else:
        product_form = ProductForm()
        
    return render(
        request, 
        "products/seller/add_product.html", 
        {"form": product_form}
    )


@login_required(login_url='/seller/login/')
@is_seller
def SellerUpdateProduct(request, prod_slug):
    try:
        product = get_object_or_404(
            Product.objects.defer('images'), 
            slug=prod_slug, 
            seller_id=request.user
        )
    except Exception:
        return HttpResponseNotFound("Product Not Found.")
    
    images = product.images.all()

    if request.method == "POST":
        product_update_form = ProductForm(request.POST, request.FILES, instance=product)

        if product_update_form.is_valid():
            product = product_update_form.save(commit=False)

            if request.POST.getlist('delete_images'):
                for image_id in request.POST.getlist('delete_images'):
                    del_image = ProductImages.objects.get(id=image_id)
                    product.images.remove(del_image)
                    del_image.delete()

            if request.FILES.getlist('new_images'):
                for image in request.FILES.getlist('new_images'):
                    product_new_image = ProductImages.objects.create(image=image)
                    product.images.add(product_new_image)

            product.save()
            return redirect(reverse('sellers:product_seller:update_product', kwargs={'prod_slug': product.slug}))
    else:
        product_update_form = ProductForm(instance=product)

    return render(
        request, 
        'products/seller/update_product.html',
        {
            'form': product_update_form, 
            'product': product, 
            'images': images
        }
    )


@login_required(login_url='/seller/login/')
@is_seller
def SellerDeleteProduct(request, prod_slug):
    try:
        product = get_object_or_404( 
            Product,
            slug=prod_slug, 
            seller_id=request.user
        )
    except Exception:
        return HttpResponseNotFound("Product Not Found.")

    for image in product.images.all():
        prod_image = ProductImages.objects.get(id=image.id)
        product.images.remove(image)
        prod_image.delete()
    
    product.delete()
    return redirect('sellers:product_seller:product_list')


@login_required(login_url="/seller/login/")
@is_seller
def SellerProductList(request):
    if request.method == "GET":
        product_search = request.GET.get('product_search')
        category_search = request.GET.get('category_search')
        product_list = Product.objects.filter(seller_id=request.user).order_by('-created_at')

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
        {'page_obj': page_obj, 'categories': categories, 'product_search': product_search}
    )
