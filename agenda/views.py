from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *
# Create your views here.


def listaAgenda(request):
    retorno = "<h1>Agendas</h1>"
    lista = Agenda.objects.all()
    for agenda in lista:
        retorno += '</br>Nome da agenda: {}</br>'.format(agenda.nome)
    return HttpResponse(retorno)

def lista_Agenda_Id(request,usuario,id):
    retorno = "<h1>Agendas</h1>"
    user= Usuario.objects.all()
    for agenda in usuario:
        if user.nome == usuario:
            Agenda = Agenda.objects.get(pk=id)
            retorno += '</br>Nome da Agenda: {}</br>'.format(agenda.nome)
    return HttpResponse(retorno)

def listaInstitucional(request):
    retorno = "<h1>Agenda Institucional</h1>"
    lista = AgendaInstitucional.objects.all()
    for agenda in lista:
        retorno += '</br>Nome da agenda: {}</br>'.format(agenda.nome)
    return HttpResponse(retorno)