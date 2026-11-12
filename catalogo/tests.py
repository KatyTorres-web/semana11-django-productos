from django.test import TestCase
from django.urls import reverse

from .models import Producto


class CatalogoViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.producto = Producto.objects.create(
            nombre='Lumi Moon',
            descripcion='Un pequeño guardián de la luna.',
            categoria='Lunar',
            precio='45.90',
            stock=12,
        )

    def test_public_pages_render(self):
        urls = (
            reverse('catalogo:inicio'),
            reverse('catalogo:lista_productos'),
            reverse('catalogo:colecciones'),
            reverse('catalogo:nosotros'),
            reverse('catalogo:contacto'),
        )

        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_home_shows_featured_product_detail_link(self):
        response = self.client.get(reverse('catalogo:inicio'))

        self.assertContains(response, self.producto.nombre)
        self.assertContains(
            response,
            reverse(
                'catalogo:detalle_producto',
                kwargs={'pk': self.producto.pk},
            ),
        )

    def test_product_list_shows_detail_link(self):
        response = self.client.get(reverse('catalogo:lista_productos'))

        self.assertContains(response, self.producto.nombre)
        self.assertContains(
            response,
            reverse(
                'catalogo:detalle_producto',
                kwargs={'pk': self.producto.pk},
            ),
        )

    def test_product_detail_renders_product(self):
        response = self.client.get(
            reverse(
                'catalogo:detalle_producto',
                kwargs={'pk': self.producto.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.producto.nombre)
        self.assertContains(response, 'Disponible: 12 unidades')

    def test_missing_product_detail_returns_404(self):
        response = self.client.get(
            reverse('catalogo:detalle_producto', kwargs={'pk': 999999})
        )

        self.assertEqual(response.status_code, 404)
