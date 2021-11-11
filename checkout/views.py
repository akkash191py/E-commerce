from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
)
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied, NotAcceptable, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers import ProductDetailSerializer
from order.models import Shipping
from order.serializers import ShippingSerializer
from cart.models import Cart, CartItem
from cart.serializers import CartItemMiniSerializer


class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        print(user)
        address_id = request.data.get("shipping")
        #print(address_id)

        #return Response({"sucess"})
        shipping_feez = 150
        user_address = Shipping.objects.filter(id=address_id, user=user)
        #user_address = Shipping.objects.filter(user=user)

        print(user_address)
        product = get_object_or_404(Product, pk=pk)
        print(product)
        total = shipping_feez + (product.price * product.quantity)
        data = {}
        #data["shipping"] = ShippingSerializer(user_address).data
        data["product"] = ProductDetailSerializer(
            product, context={"request": request}
        ).data
        data["feez"] = shipping_feez
        data["total"] = total

        return Response(data, status=status.HTTP_200_OK)


class CheckoutCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        #address_id = request.data.get("shipping")
        shipping_feez = 150
        data = {}
        total = 0
        quantity = 0
        #user_address = Shipping.objects.filter(id=address_id, user=user)[0]
        cart = get_object_or_404(Cart, user=user)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            total += item.product.price
            quantity += item.quantity
        end_total = shipping_feez + (total * quantity)

        #data["shipping"] = ShippingSerializer(user_address).data
        data["items"] = CartItemMiniSerializer(cart_items, many=True).data
        data["feez"] = shipping_feez
        data["total"] = end_total

        return Response(data, status=status.HTTP_200_OK)
