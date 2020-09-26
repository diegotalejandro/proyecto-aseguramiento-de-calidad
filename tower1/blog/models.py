from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Anuncio(models.Model):
    PRIORIDAD = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    TIPO = (
        ('0', '0'),
        ('1', '1'),
    )
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(max_length=3,
                              choices=PRIORIDAD,
                              default='1')
    categoria = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to="blog", null=True, blank=True, verbose_name="Imagen")
    autor = models.CharField(max_length=60)
    tipo_usuario = models.CharField(max_length=3,
                              choices=TIPO,
                              default='0')
    
    class Meta:
        ordering = ('-fecha',)
    def __str__(self):
        return self.titulo


