from django.db import models

# Create your models here.

class Regiao(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    
    def __str__(self):
        return "{nome}({sigla})".format(nome=self.nome,sigla=self.sigla)
        
