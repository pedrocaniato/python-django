from django.contrib import admin
from .models import Imovel, Corretor

@admin.register(Corretor)
class CorretorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'especialidade')
    search_fields = ('nome', 'email')


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'endereco', 'valor', 'tipo', 'disponivel', 'corretor')
    list_filter = ('tipo', 'disponivel', 'corretor')
    search_fields = ('titulo', 'endereco')

