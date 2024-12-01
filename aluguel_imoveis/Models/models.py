from django.db import models

class Corretor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.TextField()  # Descrição da especialidade do corretor
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    foto = models.ImageField(upload_to='corretores/', blank=True, null=True)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    TIPOS_IMOVEL = [
        ('casa', 'Casa'),
        ('apartamento', 'Apartamento'),
    ]

    titulo = models.CharField(max_length=100)
    endereco = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=15, choices=TIPOS_IMOVEL)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='imoveis/', blank=False, null=False)
    corretor = models.ForeignKey(Corretor, on_delete=models.CASCADE, related_name="imoveis")

    def __str__(self):
        return self.titulo
