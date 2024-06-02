from django.conf.urls.static import static
from django.urls import path

from apps.views import index_view, add_to_cart, show_cart, remove_cart_item, payment_options
from root import settings

urlpatterns = [
    path('', index_view, name='index_view'),
    path('add-to-cart/<int:id>', add_to_cart, name='add_to_cart'),
    path('show-cart',show_cart,name='show_cart'),
    path('cart/remove/<int:item_id>/', remove_cart_item, name='remove_cart_item'),
    path('payment/', payment_options, name='payment')
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
