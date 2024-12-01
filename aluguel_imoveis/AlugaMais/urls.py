from django.urls import path
from . import views
from .views import listar_imoveis, listar_corretores

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('homeLogado/', views.homeLogado, name='homeLogado'),
    path('imoveis/', listar_imoveis, name='listar_imoveis'),
    path('contato/', views.contato, name='contato'),
    path('quemsomos/', views.quemsomos, name='quemsomos'),
    path('corretores/', listar_corretores, name='listar_corretores'),
]
