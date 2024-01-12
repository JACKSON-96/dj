from django.test import TestCase

from django.test import TestCase
from .models import SeuModelo

class SeuModeloTestCase(TestCase):
    def setUp(self):
        SeuModelo.objects.create(nome="exemplo")

    def test_modelo_criacao(self):
        """Testa a criação de uma instância do SeuModelo."""
        exemplo = SeuModelo.objects.get(nome="exemplo")
        self.assertEqual(exemplo.nome, "exemplo")

