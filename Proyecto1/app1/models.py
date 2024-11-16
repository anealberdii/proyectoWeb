from django.db import models

# Create your models here.

class Promotor (models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='promotores/') 

    def __str__(self):
        return self.nombre
    

class Interprete (models.Model):
    nombre = models.CharField(max_length=100)
    festivales = models.ManyToManyField('Festival', related_name='interpretes_en_interprete', blank=True)
    info_general = models.TextField()
    pais = models.CharField(max_length=50)
    genero_musica = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='interpretes/') 

    def __str__(self):
        return self.nombre
    

class Festival (models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    descripcion = models.TextField()
    promotor = models.ForeignKey(Promotor, on_delete=models.CASCADE, related_name='festivales')
    interpretes = models.ManyToManyField(Interprete, related_name='festivales_en_festival', blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    foto = models.ImageField(upload_to='static/media/festivales/')   

    def __str__(self):
        return self.nombre
    

class FestivalInterprete (models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)  # Relación con el Festival
    interprete = models.ForeignKey(Interprete, on_delete=models.CASCADE)  # Relación con el Intérprete
   
    def __str__(self):
        return f"{self.interprete.nombre} en {self.festival.nombre}"
