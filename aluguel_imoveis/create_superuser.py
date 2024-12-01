
import os
import sys

def create_superuser():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aluguel_imoveis.settings')
    import django
    django.setup()

    from django.contrib.auth import get_user_model

    User = get_user_model()
    
    username = input("Digite o nome de usuário: ")
    email = input("Digite o email: ")
    password = input("Digite a senha: ")

    try:
        User.objects.create_superuser(username=username, email=email, password=password)
        print("Superusuário criado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o superusuário: {e}")

if __name__ == '__main__':
    create_superuser()
