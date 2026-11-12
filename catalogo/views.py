
from datetime import date

from django.shortcuts import render
from django.views.generic import ListView


# Datos temporales de productos
PRODUCTOS_DEMO = [
    {
        'id': 1,
        'nombre': 'Lumi Moon',
        'descripcion': 'Un pequeño guardián de la luna.',
        'categoria': 'Lunar',
        'precio': 45.90,
        'stock': 12,
        'fecha_creacion': date(2026, 11, 1),
    },
    {
        'id': 2,
        'nombre': 'Stella Bunny',
        'descripcion': 'Un conejito nacido entre estrellas.',
        'categoria': 'Estelar',
        'precio': 52.50,
        'stock': 8,
        'fecha_creacion': date(2026, 11, 2),
    },
    {
        'id': 3,
        'nombre': 'Mochi Nebulosa',
        'descripcion': 'Una criatura de una galaxia pastel.',
        'categoria': 'Galáctico',
        'precio': 59.90,
        'stock': 0,
        'fecha_creacion': date(2026, 11, 3),
    },
]


# FBV: Página de inicio
def home(request):
    contexto = {
        'titulo': 'Bienvenido a MochiVerse',
        'subtitulo': 'Un universo de ternura y magia celestial',
        'total_productos': len(PRODUCTOS_DEMO),
        'destacados': PRODUCTOS_DEMO[:2],
    }

    return render(request, 'catalogo/inicio.html', contexto)


# CBV: Catálogo de productos
class ProductoListView(ListView):
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return PRODUCTOS_DEMO

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Colección Cósmica'
        contexto['descripcion'] = (
            'Descubre a nuestros adorables guardianes del universo.'
        )
        return contexto


# FBV: Colecciones cósmicas
def colecciones(request):
    categorias = [
        {
            'nombre': 'Lunar',
            'descripcion': 'Guardianes inspirados en la luna.',
            'simbolo': '🌙',
        },
        {
            'nombre': 'Estelar',
            'descripcion': 'Personajes nacidos entre estrellas.',
            'simbolo': '⭐',
        },
        {
            'nombre': 'Galáctico',
            'descripcion': 'Criaturas de galaxias y nebulosas.',
            'simbolo': '🌌',
        },
    ]

    contexto = {
        'titulo': 'Nuestras Colecciones',
        'categorias': categorias,
    }

    return render(request, 'catalogo/colecciones.html', contexto)


# FBV: Nuestro universo
def nosotros(request):
    contexto = {
        'titulo': 'Nuestro Universo',
        'historia': (
            'MochiVerse es un universo imaginario donde '
            'pequeños guardianes celestiales representan '
            'la ternura, la creatividad y la magia de las estrellas.'
        ),
        'mision': (
            'Crear personajes coleccionables que transmitan '
            'alegría e imaginación.'
        ),
    }

    return render(request, 'catalogo/nosotros.html', contexto)


# FBV: Página de contacto
def contacto(request):
    contexto = {
        'titulo': 'Contáctanos',
        'mensaje': (
            '¿Tienes preguntas sobre nuestros guardianes cósmicos? '
            'Pronto podrás enviarnos tus mensajes.'
        ),
    }

    return render(request, 'catalogo/contacto.html', contexto)
