from django.db import models

# Create your models here.https://docs.djangoproject.com/en/4.0/ref/models/fields/

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    #nesta classe irá aparecer o nome da categoria

class Transacao(models.Model):
    data = models.DateTimeField()
    nome = models.CharField(max_length=200)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    #decimal places quantos decimais
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    #1 categoria vai poder ter várias transações. tem o one to one e o many to many tb. São 3 formas de relacionamento
    observacoes = models.TextField(null=True, blank=True)
    #nao é obrigatorio

    def __str__(self):
        return self.nome

    # coloca o que voce quer demonstrar como a descricao será mostardo lá no server em transacao

    class Meta:
        verbose_name_plural = 'Transações'
        #para trocar o nome da classe

