from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):
    user_login = serializers.CharField(max_length=100)
    user_email = serializers.EmailField()
    user_age = serializers.CharField(max_length=3)

    class Meta:
        model = Users
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_cnt = serializers.IntegerField()
    product_qty = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Products
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField()
    product_id = serializers.CharField(max_length=200)
    product_count = serializers.IntegerField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = Cart
        fields = '__all__'
