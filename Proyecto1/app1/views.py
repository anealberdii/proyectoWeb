from django.shortcuts import render, get_object_or_404
from .models import Festival, Interprete, Promotor, FestivalInterprete
from datetime import datetime

# Create your views here.
def index (request):
    promotores = Promotor.objects.all()[:6]  
    index = []
    for promotor in promotores:
        festival = Festival.objects.filter(promotor_id=promotor.id).first()
        if festival:
            index.append({'promotor': promotor, 'festival': festival})

    return render(request, 'index.html', {'index': index})


def lista_festivales(request):
    # Obtener todos los festivales como base
    festivales = Festival.objects.all()
    
    # Obtener la lista de intérpretes únicos para el menú desplegable
    artistas = Interprete.objects.all()

    # Obtener los valores de los filtros
    fecha = request.GET.get('fecha')
    artista = request.GET.get('artista')

    # Filtrar por mes y año si se proporciona la fecha
    if fecha:
        # Convertir la fecha de texto en un objeto datetime para obtener el mes y el año
        fecha_obj = datetime.strptime(fecha, "%Y-%m")
        festivales = festivales.filter(
            fecha__year=fecha_obj.year,
            fecha__month=fecha_obj.month
        )

    # Filtrar por artista si se proporciona
    if artista:
        festivales = festivales.filter(interpretes__id=artista)

    # Pasar festivales y lista de artistas al contexto
    context = {
        'festivales': festivales,
        'artistas': artistas,
    }
    return render(request, 'festivales/listaFestivales.html', context)


def detalles_festival(request, id):
    # Obtiene el festival por el ID
    festival = get_object_or_404(Festival, id=id)
    # Pasa el festival al contexto para la plantilla
    return render(request, 'festivales/detallesFestivales.html', {'festival': festival})


def lista_promotores (request):
    promotores = Promotor.objects.all()
    return render(request, 'promotores/listaPromotores.html', {'promotores': promotores})


def detalles_promotor(request, id):
    # Obtiene el promotor por el ID
    promotor = get_object_or_404(Promotor, id=id)
    
    # Filtra los festivales relacionados con el promotor por el campo promotor
    festivales = Festival.objects.filter(promotor_id=id)

    return render(request, 'promotores/detallesPromotores.html', {
        'promotor': promotor,
        'festivales': festivales
    })


def lista_interpretes (request):
    interpretes = Interprete.objects.all()
    return render(request, 'interpretes/listaInterpretes.html', {'interpretes': interpretes})


def detalles_interprete(request, id):
    # Obtén el intérprete especificado, o muestra un error 404 si no existe
    interprete = get_object_or_404(Interprete, id=id)
    
    # Obtener todos los registros de la tabla intermedia para este intérprete
    festival_interprete_entries = FestivalInterprete.objects.filter(interprete=interprete)

    # Obtener los festivales asociados a este intérprete
    festivales = [entry.festival for entry in festival_interprete_entries]

    # Renderiza la plantilla con los datos
    return render(request, 'interpretes/detallesInterpretes.html', {
        'interprete': interprete,
        'festivales': festivales
    }) 