# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response

from models import ItemAgenda

def index(request):
    return HttpResponse('Ola mundo!')

def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response('lista.html', {'lista_itens': lista_itens})

