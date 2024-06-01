from django.conf.urls.static import static
from django.urls import path

from apps.views import index_view
from root import settings

urlpatterns = [
                  path('', index_view, name='index_view')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
