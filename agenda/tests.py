"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from agenda.models import ItemAgenda
from django.contrib.auth.models import User
import datetime

class SimpleTest(TestCase):
    def setUp(self):
        usuario = User.objects.create_user('test_user', password='test_password')
        data_hora = datetime.datetime(2012, 12, 21, 20, 10)
        item = ItemAgenda.objects.create(data=data_hora.date(), hora=data_hora.time(),
            titulo="Encerramento", descricao="Fim do ano", usuario=usuario)
        item.save()

    def test_texto_amigavel(self):
        item = ItemAgenda.objects.get(titulo="Encerramento")
        texto_item = item.__str__()
        self.assertTrue("Encerramento" in texto_item)
        self.assertTrue("21/12/2012" in texto_item)
        self.assertTrue("20:10" in texto_item)

    def test_login(self):
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.get('/')
        self.assertEquals(response.status_code, 200)

    def tearDown(self):
        User.objects.all().delete()
        ItemAgenda.objects.all().delete()


