from django.db import models

# Create your models here.
class Compromisso(models.Model):
    nome= models.CharField(max_length=150)
    data= models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.nome)


class Agenda(models.Model):
    nome= models.CharField(max_length=150)
    comprmisso= models.ForeignKey(Compromisso,null = True, blank = False)

    def __str__(self):
        return '{}'.format(self.nome)

class AgendaPrivada(Agenda):
    def __str__(self):
        return '{}'.format(self.nome)

class AgendaPublica(Agenda):
    def __str__(self):
        return'{}',format(self.nome)

class AgendaInstitucional(models.Model):
    nome= models.CharField(max_length=150)
    comprmisso= models.ForeignKey(Compromisso,null = True, blank = False)
    def __str__(self):
        return '{}'.format(self.nome)

class Usuario(models.Model):
    nome= models.CharField(max_length=150,null=True,blank=False)
    agendaPrivada = models.ForeignKey(AgendaPrivada,null = True, blank = False)
    agendaPublica = models.ManyToManyField(AgendaPublica)
    agendaInstitucional = models.ManyToManyField(AgendaInstitucional)

    def __str__(self):
        return '{}'.format(self.nome)