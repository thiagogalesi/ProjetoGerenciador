# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import ItemAgenda
from forms import FormItemAgenda

def index(request):
    return HttpResponse('Ola mundo!')

def lista(request):
    lista_itens = ItemAgenda.objects.all()
    return render_to_response('lista.html', {'lista_itens': lista_itens})

def item(request, nr_item):
    item = get_object_or_404(ItemAgenda, id=nr_item)
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return render_to_response("salvo.html", {})

    return render_to_response('item.html', {'item': item})

def adiciona(request):
    if request.method == 'POST': # Formulário enviado
        form = FormItemAgenda(request.POST, request.FILES)
        if form.is_valid():
        # Formulário válido
            form.save()
            # Mensagem de formulário cadastrado
            return render_to_response("salvo.html", {})
    else:
        # Exibe formulário em branco
        form = FormItemAgenda()

    return render_to_response("adiciona.html", {'form': form}, context_instance=RequestContext(request))

