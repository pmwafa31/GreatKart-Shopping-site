from .models import Cart, CartItem
from .views import _cart_id

def cart_count(request):
    if 'admin' in request.path:
        return {}
    else:
       count = 0
       try:
           cart_item = CartItem.objects.filter(cart__cart_id=_cart_id(request))
           for cart_item in cart_item:
               count += cart_item.quantity
       except Cart.DoesNotExists():
           count = 0
    return {'count':count}