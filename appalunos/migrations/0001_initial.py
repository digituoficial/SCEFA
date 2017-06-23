# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-23 05:28
from __future__ import unicode_literals

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appPonto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Pessoa')),
                ('turno_aula', models.CharField(choices=[('Matutino', 'Matutino'), ('Vespetino', 'Vespetino'), ('Noturno', 'Noturno')], max_length=30)),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matricula')),
            ],
            options={
                'permissions': (('view_aluno', 'Can see aluno'),),
            },
            bases=('appPonto.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
