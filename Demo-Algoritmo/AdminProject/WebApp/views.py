from django.shortcuts import render
from django.http import HttpResponse
from .models import Poblacion
from django.core.files import File
from django.template.loader import render_to_string
import os 
import folium
import math
import uuid

# Create your views here.

def getUrlMaps(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.html' in file:
                data = (file[3:]).split('.')[0]
                files.append(data)
    return files

def Dashboard(request):
    
    path =  'D:\Gi-Repository\Git-Proyecto-Complejidad\TrabajoComplejidadAlgoritmica\Demo-Algoritmo\AdminProject\WebView\AlgorithmsMaps'

    files = getUrlMaps(path)

    #departamentos = Poblacion.objects.all().values_list('Departamento', flat=True).distinct()
    return render(request, 'Dashboard.html', {'files':files})

def  Map(request):
    
    idMap = str(request.GET['id'])

    path = 'AlgorithmsMaps/map'+idMap+'.html'    

    return render(request, 'Map.html',{'path':path})


# Algoritmo para calcular distancia entre 2 puntos geograficos

def ConvertToRadians(x):
    return round(x*(math.pi/180),2)

def Haversine(latOrigen, lonOrigen, latDestino, lonDestino):
    # Radio de la tierra  Radio Ecuatorial: 6378 km - Radio Polar: 6357 km - Radio Equivolumen: 6371 km
    Radio = 6378.00

    # Diferencia de latitud
    difLat = ConvertToRadians(latDestino - latOrigen)

    # Diferencia de longitud
    difLon =  ConvertToRadians(lonDestino - lonOrigen)

    a = math.sin(difLat/2)**2 + math.cos(ConvertToRadians(latOrigen))*math.cos(ConvertToRadians(latDestino))*(math.sin(difLon/2)**2)

    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distancia = round(Radio*c,2)

    return distancia


# Algoritmo de Creacion de pagina de mapeo

def CreateMap(latCentro, lonCentro ,order, tipoDeBusqueda):
    typeZoom = 0
    # Zoon map 1:World 5:Landmass/Continent 10:City 15:Streets 20: Buildings
    if tipoDeBusqueda == 'Depratmento':
        typeZoom = 5
    elif tipoDeBusqueda == 'Provincia':
        typeZoom = 8
    else: # Distrito
        typeZoom = 10

    my_map = folium.Map(location=[latCentro,lonCentro],zoom_start=typeZoom )

    points = []      

    if len(order) > 0:
        for lat, lon in order:
            points.append(tuple([lat,lon]))

        for point in points:  
            folium.Marker(point,popup='',tooltip='').add_to(my_map)

        folium.PolyLine(points, color="red", weight=1.0, opacity=1 ).add_to(my_map)

    nameOfPage = 'map'+ str(uuid.uuid4()) + '.html'

    pathComplete = 'D:/Gi-Repository/Git-Proyecto-Complejidad/TrabajoComplejidadAlgoritmica/Demo-Algoritmo/AdminProject/WebView/AlgorithmsMaps/' + nameOfPage

    my_map.save( pathComplete )

    # Procedimiento para eliminar el bootstrap 3.2.0 debido a que se esta usando bootstrap 4
    with open(pathComplete, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if 'bootstrap/3.2.0/css' not in i:
                f.write(i)
        f.truncate()

        