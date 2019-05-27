from django.shortcuts import render
from django.http import HttpResponse
from .models import Poblacion
from django.core.files import File
import os 
from django.template.loader import render_to_string

# Create your views here.

def getUrlMaps(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.html' in file:
                data = (file.split('-')[1]).split('.')[0]
                files.append("Map?idMap="+data)
    for f in files:
        print(f)
    return files



def Dashboard(request):
    path = "D:\\CURSO-COMPLEJIDAD-ALGORITMICA\\Python-Demo-Trabajo-Final\\AdminProject\\WebView\\AlgorithmsMaps"
    files = getUrlMaps(path)
    #departamentos = Poblacion.objects.all().values_list('Departamento', flat=True).distinct()
    return render(request, 'Dashboard.html', {'files':files})

def  Map(request):
    #idMap = request.GET['idMap']
    #rendered = render_to_string('AlgorithmsMaps/map-2.html')
    #print(rendered)
    html = 'AlgorithmsMaps/map-'+'2'+'.html'
    return render(request, 'Map.html')