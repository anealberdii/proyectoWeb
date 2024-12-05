from django.contrib import admin
from .models import Festival, Interprete, Promotor, Reserva

# Register your models here.

admin.site.register(Interprete)
admin.site.register(Promotor)
admin.site.register(Festival)
admin.site.register(Reserva)
