from . import views
from django.conf import settings
from django.urls import path,include
from demo.views import inicio
from django.conf.urls.static import static
urlpatterns = [
    path('',inicio.as_view(),name='inicio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)