from django.db import models

class Produtos(models.Model):

    imagem = models.FileField("imagem", upload_to="")
    nome = models.CharField("nome", max_length= 100)
    modelo = models.CharField("modelo", max_length= 40)
    descricao = models.TextField("descrição", default="Sem descrição")
    categoria = models.CharField("categoria", default="definir categoria")
    preco_unitario = models.DecimalField("preço_unitario", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} -{self.descricao} {self.preco_unitario}"