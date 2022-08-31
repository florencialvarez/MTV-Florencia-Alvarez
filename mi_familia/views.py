from re import template
from django.http import HttpResponse
from django.template import Template, Context, loader
from mi_familia.models import Familiar


def listar_familia (request):
    lista_familia= Familiar.objects.all()
    diccionario = {'familiares': lista_familia}
    plantilla = loader.get_template('lista_familia.html')
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)
