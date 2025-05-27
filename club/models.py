from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre

class Partido(models.Model):
    rival = models.CharField(max_length=100)
    fecha = models.DateField()
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.rival} - {self.fecha}"

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class Socio(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dni = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

