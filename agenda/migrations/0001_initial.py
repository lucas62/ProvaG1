# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='AgendaInstitucional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Compromisso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, null=True)),
                ('agendaInstitucional', models.ManyToManyField(to='agenda.AgendaInstitucional')),
            ],
        ),
        migrations.CreateModel(
            name='AgendaPrivada',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agenda.Agenda')),
            ],
            bases=('agenda.agenda',),
        ),
        migrations.CreateModel(
            name='AgendaPublica',
            fields=[
                ('agenda_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='agenda.Agenda')),
            ],
            bases=('agenda.agenda',),
        ),
        migrations.AddField(
            model_name='agendainstitucional',
            name='comprmisso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Compromisso'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='comprmisso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.Compromisso'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='agendaPrivada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agenda.AgendaPrivada'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='agendaPublica',
            field=models.ManyToManyField(to='agenda.AgendaPublica'),
        ),
    ]
