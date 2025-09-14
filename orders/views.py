from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from django.contrib import messages
from .models import Product 


# Create your views here.
def show_cart(request):
   user=request.user
   customer=user.customer_profile 

   cart_obj,created=Order.objects.get_or_create(
      owner=customer,
      order_status=Order.CART_STAGE
      )
   context = {'cart': cart_obj}
   return render(request,'cart.html',context)


def checkout_cart(request):
   
   if request.POST:
    
      try:
         print("inside try")
         user=request.user    
         customer=user.customer_profile   
         total=float(request.POST.get('total'))
         order_obj=Order.objects.get(
            owner=customer,
            order_status=Order.CART_STAGE
         )        
         if order_obj:
            print("inside order")
            order_obj.order_status=Order.ORDER_CONFIRMED
            print("order confirmed ")

      
            order_obj.total_price=total
            print(total)
            order_obj.save()
            print("save")
            status_message="Your order is processed. Your item will be delivered within 2 days"
            messages.success(request,status_message)
         else:
            status_message="Unable to processed. Your cart is empty order "
            messages.error(request,status_message)
      except Exception as e:
         print(user)
         print(customer)
         print(total)
         print("try exit")
         status_message="unable to procesed. No items in the cart  -- try"
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
            order_status=Order.CART_STAGE        
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

