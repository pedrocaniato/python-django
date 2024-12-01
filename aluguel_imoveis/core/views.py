from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def sobre_nos(request):
    return render(request, 'core/sobre_nos.html')

def locais_disponiveis(request):
    return render(request, 'core/locais_disponiveis.html')

def corretores(request):
    return render(request, 'core/corretores.html')

def contato(request):
    return render(request, 'core/contato.html')

# View para registro de novos usuários
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso para {username}!')
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Erro no registro. Verifique os dados e tente novamente.')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

# View para login de usuários
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
        else:
            messages.error(request, 'Erro no login. Verifique os dados e tente novamente.')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})
