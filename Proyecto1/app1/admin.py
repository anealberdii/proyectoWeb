from django.contrib import admin
from .models import Festival, Interprete, Promotor

# Register your models here.

admin.site.register(Interprete)
admin.site.register(Promotor)
admin.site.register(Festival)
