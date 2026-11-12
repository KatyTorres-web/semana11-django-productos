from django.urls import path
from django.http import HttpResponse

app_name = 'catalogo'


def inicio_temporal(request):
    return HttpResponse(
        '<h1>🌙 Bienvenido a MochiVerse</h1>'
        '<p>Tu universo de coleccionables cósmicos.</p>'
    )


def catalogo_temporal(request):
    return HttpResponse(
        '<h1>✨ Catálogo de productos</h1>'
        '<p>Explora nuestras figuras celestiales.</p>'
    )


urlpatterns = [
    path('', inicio_temporal, name='inicio'),
    path('productos/', catalogo_temporal, name='lista_productos'),
]
