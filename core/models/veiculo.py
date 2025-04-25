from django.db import models

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cor = models.ForeignKey('Cor', on_delete=models.CASCADE, related_name='veiculos')
    modelo = models.ForeignKey('Modelo', on_delete=models.CASCADE, related_name='veiculos')
    acessorios = models.ManyToManyField('Acessorio', related_name='veiculos')

    def __str__(self):
        return f'id:{self.id} {self.modelo}({self.cor}) {self.ano}'