from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemAgenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(User)
    participantes = models.ManyToManyField(User, related_name='item_participantes')

def envia_email(**kwargs):
    print ("Enviando email")

models.signals.post_save.connect(envia_email,
        sender=ItemAgenda,
        dispatch_uid="agenda.models.ItemAgenda")
