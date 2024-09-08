from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.shortcuts import get_object_or_404

from apps.forms import LoginForm, RegisterForm
from apps.models import Product, Category, CartItem



def register(request):
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            print(forms.errors)
        return redirect('login')
    return render(request, 'auth/auth.html')


def login_1(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.data.get('username')
            password = forms.data.get('password')
            users = authenticate(username=username, password=password)
            if users:
                login(request, users)
                return redirect('index_view')
            else:
                messages.add_message(request,
                                     level=messages.ERROR,
                                     message='username or password wrong'
                                     )
                return render(request, 'auth/auth.html')
    return render(request, 'auth/auth.html')



def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def index_view(request):
    pizza = get_object_or_404(Category, name='Pizza')
    pizzas = Product.objects.filter(category=pizza)
    burger = get_object_or_404(Category, name='Burger')
    burgers = Product.objects.filter(category=burger)
    kombo = get_object_or_404(Category, name='Kombo')
    kombos = Product.objects.filter(category=kombo)
    salat = get_object_or_404(Category, name='Salat')
    salats = Product.objects.filter(category=salat)
    sweet = get_object_or_404(Category, name='Sweet')
    sweets = Product.objects.filter(category=sweet)
    drink = get_object_or_404(Category, name='Drink')
    drinks = Product.objects.filter(category=drink)

    total_quantity = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Coalesce(Sum('quantity'), 0))['total_quantity']
    return render(request, 'index.html',
                  context={'pizzas': pizzas, 'burgers': burgers, 'kombos': kombos, 'salats': salats,
                           'sweets': sweets, 'drinks': drinks, 'total_quantity': total_quantity})

@login_required(login_url='/login')
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('/')

@login_required(login_url='/login')
def show_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    discount = 20  # Example fixed discount
    final_price = total_price - discount

    # Add total for each cart item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'discount': discount,
        'final_price': final_price,
    }
    return render(request, 'bs4_cart.html', context)

@login_required(login_url='/login')
def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    return redirect('show_cart')


@login_required(login_url='/login')
def payment_options(request):
    return render(request, 'payment_options.html')