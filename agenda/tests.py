"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from agenda.models import ItemAgenda
from django.contrib.auth.models import User
import datetime

class SimpleTest(TestCase):
    def setUp(self):
        usuario = User.objects.create_user('test_user', password='test_password')
        agora = datetime.datetime.now()
        item = ItemAgenda.objects.create(data=agora.date(), hora=agora.time(), titulo="Teste", 
            descricao="Descricao teste", usuario=usuario)
        item.save()

    def test_busca(self):
        item = ItemAgenda.objects.get(titulo="Teste")
        self.assertEquals(item.descricao, "Descricao teste")

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
