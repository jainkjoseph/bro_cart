from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    featured_products = Product.objects.order_by("priority")[:3]
    latest_products = Product.objects.order_by("-priority")[:3]
    context={
        'featured_products' : featured_products,
        'latest_products'   : latest_products
    }
    return render(request,'index.html',context)

def list_products(request):
    """
    products details  display

    """
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    
    """
    DISPLAY ALL
    product_list = Product.objects.all()
    TO DISPLAY PRIORITY BASED
    """
    product_list = Product.objects.order_by("priority")
    product_paginator = Paginator(product_list,3)
    product_list=product_paginator.get_page(page)
    response = render(request, 'products.html',{'products': product_list})  
    return response


    return render (request,'products.html')

def detail_product(request,pk):

    """
    product wise details - individual
    """
    product=Product.objects.get(pk=pk)
    context={'product': product}
    return render(request,'product_detail.html',context)

 