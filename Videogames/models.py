from django.db import models

# Create your models here.

class Videojuego(models.Model): 

    titulo = models.TextField(max_length = 50)
    categoria = models.TextField(max_length = 20)
    precio = models.FloatField()
    espacio_en_disco = models.IntegerField()
    fecha_alta = models.DateField()
    portada = models.ImageField(upload_to='videogames images',null=True, blank=True)
    cuerpo = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.titulo}'

