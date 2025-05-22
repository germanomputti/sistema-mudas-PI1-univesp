from django.db import models
from datetime import timedelta

class Especie(models.Model):
    nome = models.CharField(max_length=100)
    dias_ate_muda = models.PositiveIntegerField()
    dias_ate_flor = models.PositiveIntegerField()
    preco_muda = models.DecimalField(max_digits=6, decimal_places=2)
    preco_flor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class MudaPlantada(models.Model):
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    data_plantio = models.DateField()
    quantidade = models.PositiveIntegerField()

    def previsao_muda(self):
        return self.data_plantio + timedelta(days=self.especie.dias_ate_muda)

    def previsao_flor(self):
        return self.data_plantio + timedelta(days=self.especie.dias_ate_flor)

    def __str__(self):
        return f"{self.especie.nome} - {self.data_plantio}"