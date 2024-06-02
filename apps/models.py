from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, CharField, ImageField, PositiveIntegerField, ForeignKey, CASCADE


# Create your models here.


class User(AbstractUser):
    phone_number = CharField(max_length=255)

class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()
    category = ForeignKey('apps.Category', CASCADE)
    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.user.first_name}"

