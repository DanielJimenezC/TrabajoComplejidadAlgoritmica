from django.shortcuts import render
from django.http import HttpResponse
from .models import Poblacion
from . import logic as logic
from . import Algorithms as algor
# Create your views here.

def Dashboard(request):    
    path =  'D:\Gi-Repository\Git-Proyecto-Complejidad\TrabajoComplejidadAlgoritmica\Demo-Algoritmo\AdminProject\WebView\AlgorithmsMaps'

    files = logic.getUrlMaps(path)

    # departamentos = Poblacion.objects.all().values_list('Departamento', flat=True).distinct()
 
    filterDistrito = Poblacion.objects.filter(Distrito = 'SALAS')
    n = len(filterDistrito)
    
    listCiudades = [[]for _ in range(n)] # Distrito Salas
    posicionCiudades = []

    for lugar in filterDistrito:
        posicionCiudades.append(lugar.Ciudad)        

    count = 0

    for origen in filterDistrito:

        for destino in filterDistrito:

            if destino.Ciudad != origen.Ciudad:
                
                positionOrigen = logic.filtroArray(posicionCiudades,origen.Ciudad)
                positionDestino = logic.filtroArray(posicionCiudades, destino.Ciudad) 

                distancia = logic.Haversine(origen.Latitud, origen.Longitud, destino.Latitud, destino.Longitud)

                newData = algor.Viaje(positionOrigen, positionDestino, origen.Ciudad, destino.Ciudad, distancia, origen.Longitud,origen.Latitud, destino.Longitud, destino.Latitud)

                listCiudades[count].append(newData)
                
        count += 1

    algor.prim(listCiudades)
    
    return render(request, 'Dashboard.html', {'files':files})

def  Map(request):
    
    idMap = str(request.GET['id'])

    path = 'AlgorithmsMaps/map'+idMap+'.html'    

    return render(request, 'Map.html',{'path':path})



        