# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 00:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('sigla', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('ano', models.CharField(max_length=5)),
                ('logradouro', models.CharField(max_length=50)),
                ('data_de_inicio', models.DateField(null=True)),
                ('data_de_fim', models.DateField(null=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='endereco_eventos', to='eventos.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('preco', models.FloatField(null=True)),
                ('endereco', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to='eventos.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cpf', models.CharField(max_length=11)),
                ('mae', models.CharField(max_length=50)),
                ('pai', models.CharField(max_length=50)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='pessoa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='eventos.PessoaFisica'),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realizador_eventos', to='eventos.PessoaFisica'),
        ),
    ]
