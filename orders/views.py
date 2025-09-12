from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages
from . models import Product 
from . models import Customer 

# Create your views here.
def show_cart(request):
   user=request.user
   customer=user.customer_profile 

   cart_obj,created=Order.objects.get_or_create(
      owner=customer,
      rder_status=Order.CART_STAGE
      )
   context = {'cart': cart_obj}
   return render(request,'cart.html',context)


def checkout_cart(request):
   if request.POST:
 
      try:
         user=request.user
         customer=user.customer_profile
         total=float(request.POST.get('total'))
         order_obj=Order.objects.get(
         owner=customer,
         order_status=Order.CART_STAGE        
         )
         if order_obj:
            order_obj.order_status.Order. ORDER_CONFIRMED
            order_obj.total_price=total
            order_obj.save()
            status_message="Your order is processed. Your item will be delivered within 2 days"
            message.success(request,status_message)
         else:
            status_message="Unable to processed. Your cart is empty order "
            message.error(request,status_message)
      except Exception as e:
         status_message="unable to procesed. No items in the cart   try"
         messages.error(request,status_message)
   return redirect('cart')
   
def add_to_cart(request):

   if request.POST:
         user=request.user
         customer=user.customer_profile
         
         quantity=int(request.POST.get('quantity'))
         product_id=request.POST.get('product_id')
   
         cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE,
        
         )
         product=Product.objects.get(pk=product_id)
         ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj,
            quantity=quantity
         )
         if created:
            ordered_item.quantity=quantity
            ordered_item.save()
         else:
            ordered_item.quantity=ordered_item.quantity+quantity
            ordered_item.save()
         return redirect('cart')


def delete(request,pk):
   
   instance = OrderedItem.objects.get(pk=pk)
   if instance:
      instance.delete()
      return redirect('cart')

