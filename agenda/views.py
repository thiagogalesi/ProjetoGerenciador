# Create your views here.
from django.http import HttpResponse
from django.views.generic import View


class Agenda(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')
