from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome= models.CharField(max_length=150,null=True,blank=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Tipo(models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

class Agenda(models.Model):
    nome= models.CharField(max_length=150)
    usuario= models.ForeignKey(Usuario,blank=False, null=True)
    tipo= models.OneToOneField(Tipo,blank=False,null=True)
    institucional= models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.nome)

class Compartilha(models.Model):
    usuario= models.ForeignKey(Usuario,blank=False, null=True)
    agenda= models.ManyToManyField(Agenda)

class Compromisso(models.Model):
    nome= models.CharField(max_length=150)
    dataInicio= models.DateTimeField(blank=True,null=True)
    dataFim= models.DateTimeField(blank=True,null=True)
    agenda= models.ForeignKey(Agenda,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.nome)

class Convite(models.Model):
    usuarioConvida= models.ForeignKey(Usuario,related_name='Inviter',null=True,blank=True)
    usuarioConvidado= models.ForeignKey(Usuario,related_name='Convidado',null=True,blank=True)
    compromisso= models.ForeignKey(Compromisso,blank=True,null=True)
    resposta= models.BooleanField(blank=False)