from django.db import models
from garagem.models import Marca,Categoria,Cor
    
class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField( default = 0,null=True, blank=True, max_digits=10, decimal_places=2)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="veiculos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")



    def __str__(self):
        return f"{self.marca} {self.modelo} {self.ano}, {self.cor}"
    
from uploader.models import Image

class Veiculo(models.Model):
    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )