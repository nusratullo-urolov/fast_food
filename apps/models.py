from django.db import models
from django.db.models import Model, CharField, ImageField, PositiveIntegerField


# Create your models here.
class Pizza(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name


class Burger(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name

class Kombo(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name


class Salat(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name


class Sweet(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name

class Drink(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    image = ImageField(upload_to='media/')
    price = PositiveIntegerField()

    def __str__(self):
        return self.name