from django.contrib import admin
from .models import Imovel, Proprietario, Cliente, Contrato, Pagamento, Corretor

@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'preco', 'descricao')

@admin.register(Proprietario)
class ProprietarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'data_inicio', 'data_fim', 'valor')

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('contrato', 'data_pagamento', 'valor')

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'email')