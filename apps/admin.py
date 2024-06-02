from django.contrib import admin

from apps.models import Product, Category, CartItem, User

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(User)
