from django.shortcuts import render
from django.http import HttpResponse
from .models import Poblacion
from . import logic as logic
from . import Algorithms as algor
from . import data as data

# Create your views here.
def Dashboard(request):
    # Departamentos
    listaDepartamentos = data.GetProvince('APURIMAC')
    G = data.GetDataTest(listaDepartamentos)
    pi, pf = algor.DefinirPuntoInicioYFin(G)
    order = algor.UFDSModificado(G, pi, pf)
    print(order)
    # for nameDep, _, _ in listaDepartamentos:
    #     listProByDep = data.GetProvince(nameDep)
    #     G = data.GetDataTest(listProByDep)
    #     pi, pf = algor.DefinirPuntoInicioYFin(G)
    #     order = algor.UFDSModificado(G, pi, pf)
    #     dataSetMap = []
    #     for i in range(len(order)):
    #         dataSetMap.append((listProByDep[order[i]][1],listProByDep[order[i]][2]))
    #     logic.CreateMap(-9.9582944,-72.2648333, dataSetMap,'Provincia', 'Provincias-de-' + nameDep)


    
    # logic.CreateMap(-9.9582944,-72.2648333, dataSetMap, 'Departamento')
    path = 'D:\Gi-Repository\Git-Proyecto-Complejidad\TrabajoComplejidadAlgoritmica\Demo-Algoritmo\AdminProject\WebView\AlgorithmsMaps'
    files = logic.getUrlMaps(path)
    return render(request, 'Dashboard.html', {'files':files})

def  Map(request):
    
    idMap = str(request.GET['id'])

    path = 'AlgorithmsMaps/map'+idMap+'.html'    

    return render(request, 'Map.html',{'path':path})



        