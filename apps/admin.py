from django.contrib import admin

from apps.models import Pizza, Burger, Kombo, Salat, Sweet, Drink

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Burger)
admin.site.register(Kombo)
admin.site.register(Salat)
admin.site.register(Sweet)
admin.site.register(Drink)