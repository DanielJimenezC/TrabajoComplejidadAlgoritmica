#BackTracking
import heapq as pq
import math as m
def BusquedaDeRutas(G,v,visited,vp,orden):
    opciones = []
    visited[v] = True    
    orden.append(v)
    auxVisited = visited.copy()
    auxOrden = orden.copy()
    for u in G[v]:
        if visited[u] == False:
            opciones.append(u)

    for u in opciones:
        if visited[u] == False:
            BusquedaDeRutas(G,u,visited,vp,orden)
        visited = auxVisited
        orden = auxOrden        
    if all(visit == True for visit in visited) and len(opciones) == 0 and vp in G[v]:
        print(orden)   
        
def BusquedaDeRutasConPeso(G,v,visited,vp,orden,sumDistancia,distanciaFinal):
    opciones = []
    visited[v] = True    
    orden.append(v)
    auxVisited = visited.copy()
    auxOrden = orden.copy()
    auxsumDistancia  = sumDistancia 
    count = 0
    for item in G[v]:
        if visited[item[1]] == False:
            opciones.append((item[1],count))
        count += 1
    
    for item in opciones:        
        if visited[item[0]] == False:
            sumDistancia += (((G[v])[item[1]])[0])            
            BusquedaDeRutasConPeso(G,item[0],visited,vp,orden,sumDistancia,distanciaFinal)
        visited = auxVisited
        orden = auxOrden    
        sumDistancia = auxsumDistancia 

    validacion = []    
    for x in G[v]:
        validacion.append(x[1])

    if all(visit == True for visit in visited) and len(opciones) == 0  and vp in validacion :
        #print(sumDistancia) 
        #print(orden)
        distanciaFinal.append((sumDistancia,orden))
    return distanciaFinal
    
        

G = [
    [2,3,4],
    [3,4],
    [0,4],
    [0,2],
    [2,1]
]

G2 = [
    [(100,2),(40,3),(10,4)],
    [(20,3),(50,4)],
    [(15,0),(35,4)],
    [(22,0),(10,2)],
    [(14,2),(23,1)]
]

    
    
#hola.append(list(y[1] for y in x ) for x in G2 )

n = len(G)
#BusquedaDeRutas(G,1,[False]*n,1,[])
posiblesResultados = BusquedaDeRutasConPeso(G2,1,[False]*n,1,[],0,[])
result = []
for data in posiblesResultados:
    pq.heappush(result,data)
print(pq.heappop(result))



def CalcularDistancia(lat1,lon1,lat2,lon2):
    return m.sqrt((lat1-lat2)**2)+((lon1-lon2)**2)
