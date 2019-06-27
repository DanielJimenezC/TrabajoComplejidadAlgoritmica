from django.db import connection
from . import logic as logic

def GetDepartments():
    with connection.cursor() as cursor:
        cursor.execute('select distinct("Departamento") as "Departamento", first_value("Latitud") over (partition by "Departamento" order by "Departamento" asc ) as "Latitud", first_value("Longitud") over (partition by "Departamento" order by "Departamento" asc) as "Longitud" from "WebApp_poblacion"')
        row = cursor.fetchall()
    return row

def GetProvince(nameDepartment):
    with connection.cursor() as cursor:
        cursor.execute('select distinct("Provincia"), first_value("Latitud") over (partition by "Provincia" order by "Provincia" asc ) as "Latitud", first_value("Longitud") over (partition by "Provincia" order by "Provincia" asc) as "Longitud" from "WebApp_poblacion" where "Departamento" =  %s ', [nameDepartment])
        row = cursor.fetchall()
    return row

def GetDistricts(nameDepartment, nameProvince):
    with connection.cursor() as cursor:
        cursor.execute('select distinct("Distrito"), first_value("Latitud") over (partition by "Distrito" order by "Distrito" asc ) as "Latitud", first_value("Longitud") over (partition by "Distrito" order by "Distrito" asc) as "Longitud" from "WebApp_poblacion" where "Departamento" =  %s and "Provincia" = %s', [nameDepartment, nameProvince])
        row = cursor.fetchall()
    return row


def GetCities(nameDepartment, nameProvince, nameDistrict):
    with connection.cursor() as cursor:
        cursor.execute('select "Ciudad", "Latitud", "Longitud" from "WebApp_poblacion" where "Departamento" = %s and "Provincia" = %s  and "Distrito" = %s', [nameDepartment,nameProvince, nameDistrict])
        row = cursor.fetchall()
    return row


def GetDataTest(lista):

    n = len(lista)

    posicionLugares = []
    for name, _, _ in lista:
        posicionLugares.append(name)

    listDataTest = [[] for _ in range(n)]
    for origenName, origenLat, origenLon in lista:
        for destinyName, destinyLat, destinyLon in lista:
            if origenName != destinyName:
                positioOrigen = logic.filtroArray(posicionLugares, origenName)
                positionDestiny = logic.filtroArray(posicionLugares, destinyName)

                distancia = logic.Haversine(origenLat, origenLon, destinyLat, destinyLon)
                listDataTest[positioOrigen].append((positionDestiny,distancia))

    return listDataTest
