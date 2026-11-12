
from django.urls import path

from .views import (
    home,
    ProductoListView,
    colecciones,
    nosotros,
    contacto,
)

app_name = 'catalogo'

urlpatterns = [
    path('', home, name='inicio'),

    path(
        'productos/',
        ProductoListView.as_view(),
        name='lista_productos'
    ),

    path(
        'colecciones/',
        colecciones,
        name='colecciones'
    ),

    path(
        'nosotros/',
        nosotros,
        name='nosotros'
    ),

    path(
        'contacto/',
        contacto,
        name='contacto'
    ),
]
