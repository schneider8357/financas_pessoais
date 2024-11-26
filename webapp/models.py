from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=500)
    valor_orcado = models.DecimalField(max_digits=6, decimal_places=2)
    data_vencimento = models.DateField()
    data_compra = models.DateField()
    TIPO_LANCAMENTO_CHOICES = {
        "RE": "Receita",
        "DE": "Despesas Essenciais",
        "NE": "Despesas Não Essenciais",
        "IN": "Investimentos",
    }
    tipo_lancamento = models.CharField(max_length=2, choices=TIPO_LANCAMENTO_CHOICES)
    CATEGORIA_CHOICES = {
        "SAL": "Salários",
        "COM": "Comissões",
        "ALU": "Aluguel",
        "AGU": "Água",
        "LUZ": "Luz",
    }
    categoria = models.CharField(max_length=3, choices=CATEGORIA_CHOICES)
    STATUS_CHOICES = {
        "A": "A pagar",
        "P": "Pago"
    }
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
