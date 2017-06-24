# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-24 16:19
from __future__ import unicode_literals

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_funcao', models.CharField(max_length=200, verbose_name='Nome da função')),
            ],
            options={
                'permissions': (('view_cargo', 'Can see cargo'),),
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200, verbose_name='Descrição')),
            ],
            options={
                'permissions': (('view_departamento', 'Can see departamento'),),
            },
        ),
        migrations.CreateModel(
            name='Dias_sem_expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('hora_entrada', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('hora_saida', models.TimeField(default=django.utils.timezone.now, null=True)),
                ('local', models.CharField(max_length=200, null=True, verbose_name='local')),
                ('observacao', models.CharField(max_length=200, null=True, verbose_name='Observação')),
                ('inconsistencia', models.CharField(max_length=200, null=True, verbose_name='Inconsistencia')),
            ],
            options={
                'permissions': (('view_frequencia', 'Can see frequencia'), ('view_frequencia_admin', 'Can see frequencia a mais')),
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('Email', models.EmailField(max_length=200, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('senha', models.CharField(max_length=32)),
                ('situacao',
                 models.CharField(choices=[('Ativo', 'Ativo'), ('Desativado', 'Desativado')], max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos', verbose_name='foto')),
            ],
            options={
                'permissions': (('view_pessoa', 'Can see pessoa'),),
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='appPonto.Pessoa')),
                ('matricula', models.CharField(max_length=10, unique=True, verbose_name='Matricula')),
            ],
            options={
                'permissions': (('view_funcionario', 'Can see funcionario'),),
            },
            bases=('appPonto.pessoa',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='frequencia',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Pessoa'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Departamento', verbose_name='Departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cargo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPonto.Cargo', verbose_name='Cargo'),
        ),
    ]
