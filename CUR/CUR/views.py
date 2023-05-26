from django.http import HttpResponse
from django.template import Template,Context
# -*- coding: utf-8 -*-

def home(request):
    plantillaExterna = open("C:/Users/USER/Desktop/CUR/CUR/plantillas/index.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)