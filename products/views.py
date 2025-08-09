from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    """
    products details  display

    """
    page = 1
    if request.GET:
        page = request.GET.get('page',1)
    
   
    product_list = Product.objects.all()

    product_paginator = Paginator(product_list,3)
    product_list=product_paginator.get_page(page)
    response = render(request, 'products.html',{'products': product_list})  
    return response


    return render (request,'products.html')

def detail_product(request):

    """
    product wise details - individual
    """
    return render(request,'product_detail.html')

 