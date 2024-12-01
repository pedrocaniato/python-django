import uuid
from django.db import models
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename



class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    endereco = models.CharField(max_length=255,default='Endereço não informado')
    foto = StdImageField(('Foto'), null=True, blank=True, upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    def __str__(self):
        return self.nome

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Contrato(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f" Contrato de {self.cliente.nome} para {self.imovel.nome}"

class Pagamento(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    data_pagamento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pagamento de {self.valor} em {self.data_pagamento}"

class Corretor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Imobiliaria(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255, default='Endereço não informado')
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
