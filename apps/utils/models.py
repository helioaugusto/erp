from django.db import models

# Create your models here.

class Regiao(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    
    class Meta:
        verbose_name = "Região"
        verbose_name_plural = "Regiões"
    
    def __str__(self):
        return "{nome}({sigla})".format(nome=self.nome,sigla=self.sigla)
   
    
class Estado(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    sigla = models.CharField(max_length=2, unique=True)
    regiao = models.ForeignKey(Regiao)
    
    def __str__(self):
        return "{nome}".format(nome=self.nome)


class Cidade(models.Model):
    nome = models.CharField(max_length=32, unique=True)
    ddd = models.CharField(max_length=2, unique=True)
    estado = models.ForeignKey(Estado)
        
    def __str__(self):
        return "{nome}({estado})".format(nome=self.nome, estado=self.estado)
        
