from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def list_products(request):
    """
    products details  display
    """
    return render (request,'products.html')

def detail_product(request):

    """
    product wise details - individual
    """
    return render(request,'product_detail.html')

 