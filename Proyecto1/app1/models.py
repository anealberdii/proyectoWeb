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
    fotoFondo = models.ImageField(upload_to='interpretes/')  

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
    foto = models.ImageField(upload_to='festivales/')
    entradasDisponibles = models.PositiveIntegerField()   

    def __str__(self):
        return self.nombre
    

class FestivalInterprete (models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE)  # Relación con el Festival
    interprete = models.ForeignKey(Interprete, on_delete=models.CASCADE)  # Relación con el Intérprete
   
    def __str__(self):
        return f"{self.interprete.nombre} en {self.festival.nombre}"

class Reserva (models.Model):
    festival = models.ForeignKey(Festival, on_delete=models.CASCADE, related_name="reservas")  # Relación con Festival
    nombre = models.CharField(max_length=100)  # Nombre del cliente
    apellidos = models.CharField(max_length=150)  # Apellidos del cliente
    email = models.EmailField()  # Email del cliente
    telefono = models.CharField(max_length=15)  # Teléfono del cliente
    direccion = models.TextField(blank=True, null=True)  # Dirección (puede ser opcional)
    localidad = models.CharField(max_length=100, blank=True, null=True)  # Localidad (opcional)
    numEntradas = models.PositiveIntegerField()  # Número de entradas reservadas
    fechaReserva = models.DateTimeField(auto_now_add=True)  # Fecha y hora de la reserva

    class Meta:
        db_table = 'app1_reservas'  # Nombre explícito de la tabla en la base de datos
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.numEntradas} entradas para {self.festival.nombre}"