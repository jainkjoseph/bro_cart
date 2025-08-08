from django.shortcuts import render
from . models import Product

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    """
    products details  display
    """
    product_list = Product.objects.all()

    print(product_list)
    response = render(request, 'products.html',{'products': product_list})  
    return response


    return render (request,'products.html')

def detail_product(request):

    """
    product wise details - individual
    """
    return render(request,'product_detail.html')

 