from . import views
from django.urls import path,include
from demo.views import inicio
urlpatterns = [
    path('',inicio.as_view(),name='inicio'),
]