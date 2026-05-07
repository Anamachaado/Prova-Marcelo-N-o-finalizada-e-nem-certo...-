from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.nome

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    dataPublicada = models.DateField(auto_now_add=True)
    autor = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='post_categoria')
    def __str__(self):
        return self.titulo