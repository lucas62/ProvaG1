from django.contrib import admin
from agenda.models import *
# Register your models here.

admin.site.register(Compromisso)
admin.site.register(Agenda)
admin.site.register(AgendaPrivada)
admin.site.register(AgendaPublica)
admin.site.register(AgendaInstitucional)
admin.site.register(Usuario)