from django import template

register = template.Library()

@register.simple_tag(name='grandtotal')
def grandtotal(cart):
    total=0 
    for items in cart.added_items.all():
        total+=items.quantity*items.product.price
        print(total)
    return total


