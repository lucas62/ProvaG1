from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from processo.models import *
from processo.serializers import *

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class VagaViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer