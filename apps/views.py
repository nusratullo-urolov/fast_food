from django.shortcuts import render

from apps.models import Pizza, Burger, Kombo, Salat, Sweet, Drink


# Create your views here.
def index_view(request):
    pizzas = Pizza.objects.order_by('-id')
    burgers = Burger.objects.order_by('-id')
    kombos = Kombo.objects.order_by('-id')
    salats = Salat.objects.order_by('-id')
    sweets = Sweet.objects.order_by('-id')
    drinks = Drink.objects.order_by('-id')
    return render(request, 'index.html',
                  context={'pizzas': pizzas, 'burgers': burgers, 'kombos': kombos, 'salats': salats,
                           'sweets': sweets, 'drinks': drinks})


def pizza(request):
    pizzas = Pizza.objects.order_by('-id')
    return render(request, 'pizza.html', context={'pizzas': pizzas})
