from django.db import models


class Users(models.Model):
    user_login = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_age = models.CharField(max_length=3)

    class Meta:
        db_table = "Users"


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    product_cnt = models.IntegerField()
    product_qty = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = "Products"


class Cart(models.Model):
    user_email = models.EmailField()
    product_id = models.IntegerField()
    product_count = models.IntegerField()
    product_quantity = models.IntegerField()

    class Meta:
        db_table = "Cart"
