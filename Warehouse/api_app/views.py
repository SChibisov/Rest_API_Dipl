from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from django.shortcuts import get_object_or_404

from .service import CartService


class CartViews(APIView):

    def post_cart(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    """
    $ curl -X GET http://127.0.0.1:8000/api/cart-items/1
    $ curl -X GET http://127.0.0.1:8000/api/cart-items/
    """
    def get_cart(self, request, id=None):
        if id:
            item = Cart.objects.get(id=id)
            serializer = CartSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Cart.objects.all()
        serializer = CartSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    """
    $ curl -X PATCH http://127.0.0.1:8000/api/cart-items/1 -H 'Content-Type: 
    application/json' -d '{"product_quantity":6}'
     """
    def patch_cart(self, request, id=None):
        item = Cart.objects.get(id=id)
        serializer = CartSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    """$ curl -X "DELETE" http://127.0.0.1:8000/api/cart-items/1"""
    def delete_cart(self, request, id=None):
        item = get_object_or_404(Cart, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class CartAPI(APIView):
    def get(self, request):
        cart = CartService(request)

        return Response(
            {"data": list(cart.__len__()),
             },
            status=status.HTTP_200_OK
        )

    def post(self, request, **kwargs):
        cart = CartService(request)

        if "remove" in request.data:
            product = request.data["product"]
            cart.remove(product)

        elif "clear" in request.data:
            cart.clear()

        else:
            product = request.data
            cart.add(
                product=product["product"],
                quantity=product["quantity"],
                overide_quantity=product["overide_quantity"] if "overide_quantity" in product else False
            )

        return Response(
            {"message": "cart updated"},
            status=status.HTTP_202_ACCEPTED)
