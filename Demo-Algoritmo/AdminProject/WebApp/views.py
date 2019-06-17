from django.shortcuts import render
from django.http import HttpResponse
from .models import Poblacion
from . import logic as logic
# Create your views here.

def Dashboard(request):
    
    path =  'D:\Gi-Repository\Git-Proyecto-Complejidad\TrabajoComplejidadAlgoritmica\Demo-Algoritmo\AdminProject\WebView\AlgorithmsMaps'

    files = logic.getUrlMaps(path)

    #departamentos = Poblacion.objects.all().values_list('Departamento', flat=True).distinct()
    return render(request, 'Dashboard.html', {'files':files})

def  Map(request):
    
    idMap = str(request.GET['id'])

    path = 'AlgorithmsMaps/map'+idMap+'.html'    

    return render(request, 'Map.html',{'path':path})



        