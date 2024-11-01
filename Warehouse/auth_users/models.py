from django.db import models


class Users(models.Model):
    objects = None
    user_id = models.IntegerField()
    user_login = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_age = models.CharField(max_length=3)

    class Meta:
        db_table = "Users"
