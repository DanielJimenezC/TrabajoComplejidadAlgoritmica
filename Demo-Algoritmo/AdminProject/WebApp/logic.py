import os 
import folium
import math
import uuid

# Obtener los archivos segun el path establecido
def getUrlMaps(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.html' in file:
                data = (file[3:]).split('.')[0]
                files.append(data)
    return files


# Algoritmo para calcular distancia entre 2 puntos geograficos
def ConvertToRadians(x):
    return x * (math.pi / 180)

def Haversine(latOrigen, lonOrigen, latDestino, lonDestino):
    # Radio de la tierra  Radio Ecuatorial: 6378 km - Radio Polar: 6357 km - Radio Equivolumen: 6371 km
    Radio = 6378.00

    # Diferencia de latitud
    difLat = (latDestino - latOrigen)

    # Diferencia de longitud
    difLon =  (lonDestino - lonOrigen)

    a = (math.sin(ConvertToRadians(difLat)/2))**2 + math.cos(ConvertToRadians(latOrigen))*math.cos(ConvertToRadians(latDestino))*((math.sin(ConvertToRadians(difLon)/2))**2)

    # c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    distancia = 2*Radio*math.asin(math.sqrt(a))

    return round(distancia, 2)


# Algoritmo de Creacion de pagina de mapeo
def CreateMap(latCentro, lonCentro ,order, tipoDeBusqueda, nameFile):
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

    if nameFile == '':
        nameOfPage = 'map'+ str(uuid.uuid4()) + '.html'
    else:
        nameOfPage = 'map-'+str(nameFile)+'.html'

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


# Funcion de filtro
def filtroArray(array, filtro):
    i = 0
    for data in array:
        if data == filtro:
            return i
        i += 1
    return None

    