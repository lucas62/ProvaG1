from django.contrib import admin
from processo.models import *

# Register your models here.

admin.site.register(Eleicao)
admin.site.register(Eleitor)
admin.site.register(Vaga)
admin.site.register(Candidato)
admin.site.register(Voto)
admin.site.register(Token)
admin.site.register(Resultado)