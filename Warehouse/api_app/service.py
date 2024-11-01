from decimal import Decimal
from django.conf import settings
from .serializers import CartSerializer
from .models import Cart


class CartService:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1, overide_quantity=False):
        product_id = str(product[id])
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_quantity': 0,
            }
        if overide_quantity:
            self.cart[product_id]['product_quantity'] = quantity
        else:
            self.cart[product_id]['product_quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product[id])

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __len__(self):
        return sum(item['product_quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
