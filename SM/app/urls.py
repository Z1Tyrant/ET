from django.urls import path
from .views import index, cuenta, carrito, api, inicio, objetos, recuperar, soporte, souls

urlpatterns = [
    path('', index, name="index"),
    path('cuenta/', cuenta, name="cuenta"),
    path('carrito/', carrito, name="carrito"),
    path('api/', api, name="api"),
    path('inicio/', inicio, name="inicio"),
    path('objetos/', objetos, name="objetos"),
    path('recuperar/', recuperar, name="recuperar"),
    path('soporte/', soporte, name="soporte"),
    path('souls/', souls, name="souls"),
]