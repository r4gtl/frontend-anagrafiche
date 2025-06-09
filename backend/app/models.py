from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    partita_iva = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Fornitore(models.Model):
    nome = models.CharField(max_length=200)
    partita_iva = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
