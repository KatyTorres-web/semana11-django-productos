
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Producto


# FBV: Página de inicio
def home(request):
    contexto = {
        'titulo': 'Bienvenido a MochiVerse',
        'subtitulo': 'Un universo de ternura y magia celestial',
        'total_productos': Producto.objects.count(),
        'destacados': Producto.objects.filter(
            stock__gt=0
        )[:2],
    }

    return render(request, 'catalogo/inicio.html', contexto)


# CBV: Catálogo de productos
class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto['titulo'] = 'Colección Cósmica'
        contexto['descripcion'] = (
            'Descubre a nuestros adorables guardianes del universo.'
        )

        return contexto


# CBV: Detalle individual del producto
class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'catalogo/detalle.html'
    context_object_name = 'producto'


# FBV: Colecciones
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
