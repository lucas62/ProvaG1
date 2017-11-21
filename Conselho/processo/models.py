from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Eleicao(models.Model):
    nome = models.CharField(max_length=50,null=True,blank=False)
    data_Inicio = models.DateTimeField("Data Inicio", null=True,blank=False)
    data_Fim = models.DateTimeField("Data Fim", null=True,blank=False)
    local = models.CharField(max_length=100,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Token(models.Model):
    eleicao = models.ForeignKey(Eleicao,null=True,blank=False)
    data_Emissao = models.DateTimeField(null=True,blank=False)
    verificado = models.BooleanField("Já votou?",default=False)#True já votou.

    def __str__(self):
        return '{}'.format(self.verificado)

class Eleitor(models.Model):
    user = models.ForeignKey(User,null=True,blank=False)
    token = models.ForeignKey(Token,null=True,blank=False)
    nome = models.CharField(max_length=100,null=True,blank=False)
    CPF = models.CharField(max_length=11,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Vaga(models.Model):
    nome = models.CharField(max_length=50,null=True,blank=False)
    descricao = models.TextField(max_length=500,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Candidato(models.Model):
    nome = models.CharField(max_length=100,null=True,blank=False)
    cpf = models.CharField(max_length=11,null=True,blank=False)
    rg  = models.CharField(max_length=15,null=True,blank=False)
    codigo_Candidatura = models.CharField("Código de Candidatura",max_length=9,null=True,blank=False)
    vaga = models.ForeignKey(Vaga,null=True,blank=False)

    def __str__(self):
        return '{} - {}'.format(self.codigo_Candidatura,self.nome)

class Voto(models.Model):
    VOTO_CHOICES = (
        ('sim', 'SIM'),
        ('voto em branco', 'VOTO EM BRANCO'),
    )
    voto = models.CharField(max_length=14, choices=VOTO_CHOICES, blank=False, null=False)
    eleicao = models.ForeignKey(Eleicao,null=True,blank=False)
    candidato = models.ForeignKey(Candidato,null=True,blank=False)
    data_Voto = models.DateTimeField("Data do Voto", null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.candidato.nome)

class Resultado(models.Model):
    eleicao = models.ForeignKey(Eleicao,null=True,blank=False)
    candidato = models.ForeignKey(Candidato,null=True,blank=False)
    tota_Voto = models.FloatField(null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.candidato.nome)