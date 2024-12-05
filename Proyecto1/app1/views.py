from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Festival, Interprete, Promotor, FestivalInterprete, Reserva
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

    festival = get_object_or_404(Festival, id=id)

    return render(request, 'festivales/detallesFestivales.html', {
        'festival': festival,
        'entradasDisponibles': festival.entradasDisponibles,
    })


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


def formulario(request, id):  
    # Obtener el festival según el id
    festival = get_object_or_404(Festival, id=id)

    if request.method == 'POST':
        # Recuperar los datos del formulario
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion', '')
        localidad = request.POST.get('localidad', '')
        numeroEntradas = request.POST.get('numero_entradas')  # Este será el campo del número de entradas
        aceptoTerminos = request.POST.get('acepto_terminos') == 'true'

        # Verificar si el campo número de entradas está vacío o no es válido
        if not numeroEntradas:
            return JsonResponse({'success': False, 'error': 'Por favor, ingrese el número de entradas.'})
        
        # Convertir el número de entradas a entero, si no es válido mostrar error
        try:
            numeroEntradas = int(numeroEntradas)
        except ValueError:
            return JsonResponse({'success': False, 'error': 'Número de entradas no válido.'})
        
        # Validar disponibilidad de entradas
        if numeroEntradas > festival.entradasDisponibles:
            return JsonResponse({'success': False, 'error': 'No hay suficientes entradas disponibles.'})

        # Guardar la reserva en la base de datos
        reserva = Reserva(
            festival=festival,
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono,
            direccion=direccion,
            localidad=localidad,
            numEntradas=numeroEntradas,
        )
        reserva.save()

        # Actualizar las entradas disponibles del festival
        festival.entradasDisponibles -= numeroEntradas
        festival.save()

        # Responder con éxito
        return JsonResponse({'success': True, 'message': '¡Compra realizada correctamente! Muchas gracias.'})

    return render(request, 'formulario.html', {'festival': festival})