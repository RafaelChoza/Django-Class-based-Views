from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    price = models.FloatField()

class Usuario(models.Model):
    usuario = models.CharField(max_length=128)
    correo = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)