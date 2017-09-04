from django.db import models
from django.contrib.auth.models import User

class Endereco(models.Model):
    logradouro = models.CharField(max_length=128)
    complemento = models.CharField(max_length=256, null=True)
    uf = models.CharField(max_length=2,null=True)
    cidade = models.CharField(max_length=64, null=True)
    cep = models.CharField(max_length=10)
    usuario = models.OneToOneField(User) 
    def __str__(self):
        return '{} - {}, {}'.format(self.logradouro,self.cidade,self.uf)

class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.ForeignKey(Endereco, related_name='pessoas', null=True, blank=False)
    def __str__(self):
        return self.nome

class PessoaFisica (Pessoa):
    cpf = models.CharField(max_length=11)
    mae = models.CharField(max_length=50)
    pai = models.CharField(max_length=50)

class Evento (models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    sigla = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)
    ano = models.CharField(max_length=5)
    realizador = models.ForeignKey(PessoaFisica, related_name='realizador_eventos', null=True, blank=False)
    endereco = models.ForeignKey(Endereco, related_name='endereco_eventos', null=True, blank=False)
    logradouro = models.CharField(max_length=50)
    data_de_inicio = models.DateField( null=True)
    data_de_fim = models.DateField( null=True)

class Inscricao(models.Model):
    endereco = models.ForeignKey(Endereco, related_name='inscricao', null=True, blank=False)
    pessoa = models.ForeignKey(PessoaFisica,related_name='participantes', null=True, blank=False)
    data = models.DateField(null=True)
    preco = models.FloatField(null=True)

    class Meta ():
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'