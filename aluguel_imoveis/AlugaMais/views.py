from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_django
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User
from Models.models import Imovel, Corretor


def listar_corretores(request):
    corretores = Corretor.objects.all() 
    return render(request, 'corretores.html', {'corretores': corretores})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')

        # Verifica se o CPF já está cadastrado
        if User.objects.filter(username=cpf).exists():
            return HttpResponse('Já existe um cliente com esse CPF.')

        # Verifica se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            return HttpResponse('Já existe um cliente com esse email.')

        # Valida se as senhas são iguais
        if senha != confirmacao_senha:
            return HttpResponse('As senhas não conferem.')

        try:
            # Cria o usuário no banco
            user = User.objects.create_user(
                username=cpf,
                first_name=nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            user.save()
            return HttpResponse('Cliente cadastrado com sucesso!')
        except Exception as e:
            return HttpResponse(f'Ocorreu um erro ao cadastrar o cliente: {e}')


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        # Autentica o usuário com o CPF (usado como username)
        user = authenticate(username=cpf, password=senha)

        if user is not None:
            # Login do usuário
            login_django(request, user)
            return redirect('homeLogado')
        else:
            return HttpResponse('CPF ou senha inválidos.')


def homeLogado(resquest):
    return render (resquest,'homeLogado.html')

def imoveis(resquest):
    return render (resquest,'imoveis.html')

def contato(resquest):
    return render (resquest,'contato.html')


def quemsomos(resquest):
    return render (resquest,'quemsomos.html')

def corretores(resquest):
    return render (resquest,'corretores.html')

def listar_imoveis(request):
    imoveis = Imovel.objects.all()  # Busca todos os imóveis no banco de dados
    tipo = request.GET.get('tipo')
    valor_max = request.GET.get('valorMax')

    # Filtragem
    if tipo:
        imoveis = imoveis.filter(tipo=tipo)
    if valor_max:
        imoveis = imoveis.filter(valor__lte=valor_max)

    return render(request, 'imoveis.html', {'imoveis': imoveis})