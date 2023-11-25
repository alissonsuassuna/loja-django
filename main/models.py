from django.db import models

class Marca(models.Model):

    nome = models.CharField('Nome da Marca', max_length=100)

    #nome dos objetos de modelo
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField('Nome do Produto', max_length=100)
    descricao = models.TextField('Descrição do Produto', blank=True, null=True) #não obrigatorio
    preco = models.DecimalField('Preço  do produto',max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque do produto', default=50) #nome padrao
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nome