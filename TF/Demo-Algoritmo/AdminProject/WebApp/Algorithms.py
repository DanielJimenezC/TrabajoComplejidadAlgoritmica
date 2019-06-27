#Algoritmo PRIM
import heapq as hq
import math
from math import sqrt
from heapq import heappop, heappush
from . import logic as logic
INF = math.inf

class Viaje:
    def __init__(self, posOrigen, posDestino, lugarOrigen, lugarDestino, distancia, lonOrigen, latOrigen, lonDestino, latDestino):
        self.posOrigen = posOrigen
        self.posDestino = posDestino
        self.lugarOrigen = lugarOrigen
        self.lugarDestino = lugarDestino
        self.distancia = distancia
        self.lonOrigen = lonOrigen
        self.latOrigen = latOrigen
        self.lonDestino = lonDestino
        self.latDestino = latDestino
    
    def getCiudad(self):
        return self.lugarOrigen


import math 
INF = math.inf

def DefinirPuntoInicioYFin(G):
    n = len(G)
    maxi = -1
    pi = 0
    pf = 0
    for i in range(n):
        for v, w in G[i]:
            print('valores ' + str(w))
            if w > maxi:              
                maxi = w
                pi = i
                pf = v
    print('maximo ' + str(maxi))
    return pi, pf 

def Union(G, a, b):
    G[b] = a

def find(G, i):
    if G[i] == i:
        return i
    else:
        #G[i] = find(G,G[i])
        return find(G,G[i])

def CheckHaveMin(G, s, path):
    mini = INF
    posFinal = -1
    for v, w in G[s]:
        if w < mini and (find(path, s) != find(path, v)):            
            mini = w
            posFinal = v
    if posFinal != -1:
        Union(path, s, posFinal)
    return posFinal
    
def SearchWay(G,s,e,indexUnion,visited,orden,sumDistancia,distanciaFinal, path):
    opciones = []
    if indexUnion != -1:
        Union(path, v, indexUnion)
    visited[s] = True    
    orden.append(s)
    auxPath = path
    auxVisited = visited.copy()
    auxOrden = orden.copy()
    auxsumDistancia  = sumDistancia 
    for v, w in G[s]:
        if find(path, v) != s:
            opciones.append((v, w))
    
    for v, w in opciones:        
        if find(path, v) != s:
            sumDistancia += w            
            SearchWay(G,s,e,v ,visited,orden,sumDistancia,distanciaFinal, path)
        visited = auxVisited
        orden = auxOrden    
        sumDistancia = auxsumDistancia 

    validacion = []    
    for x in G[v]:
        validacion.append(x[1])

    if all(visit == True for visit in visited) and len(opciones) == 0  and e in validacion :
        #print(sumDistancia) 
        #print(orden)
        distanciaFinal.append((sumDistancia,orden))
    return distanciaFinal

def UFDSModificado(G, s , e):
    n = len(G)
    path = [x for x in range(n)]
    order = []
    pos = s
    order.append(pos)
    while True:
        for _ in range(n):
            pos = CheckHaveMin(G, pos, path)
            if pos != -1:
                order.append(pos)
        if pos == e:
            return order 
    

#region KRUSKAL
# def find(G, a):
#     if G[a] < 0:
#         return a
#     else:
#         granpa = find(G, G[a])
#         G[a] = granpa
#         return granpa

# def union(G,a,b):
#     pa = find(G,a)
#     pb = find(G,b)
#     if pa != pb:
#         if G[pa] <= G[pb]:
#             G[pa] += G[pb]
#             G[pb] = pa
#         elif G[pb] < G[pa]:
#             G[pb] += G[pa]
#             G[pa] = pb

# def makeIl(G):
#     il = []
#     n = len(G)
#     for u in range(n):
#         for v, w in G[u]:
#             il.append((w, u, v))
#     return il

# def kruskal(G):
#     il = makeIl(G)
#     q = []
#     n = len(G)
#     for edge in il:
#         hq.heappush(q,edge)
#     path = [-1]*n
#     T = []
#     while len(q) > 0:
#         w, u, v = hq.heappop(q)
#         if find(path, u) != find(path, v):
#             union(path, u, v)
#             T.append((u,v,w))
#     return path, T

#endregion
#region PRIM
# def prim(G):
#     n = len(G)
#     visited = [False]*n
#     path = [-1]*n
#     cost = [INF]*n
#     queue = []
#     s = 0
#     cost[s] = 0
#     hq.heappush(queue,(0,s))
#     while len(queue) > 0:
#         _, u = hq.heappop(queue)
#         if not visited[u]:
#             visited[u] = True
#             for v, w in G[u]:
#                 if not visited[v] and w < cost[v]:
#                     path[v] = u
#                     cost[v] = w
#                     hq.heappush(queue, (w, v))

#     return path, cost
#endregion
#region DIJSTRAK
# def dijstrak(G, a):
#     n = len(G)
#     visited = [False]*n
#     path = [-1]*n
#     cost = [INF]*n
#     q = []
#     cost[a] = 0
#     hq.heappush(q, (0,a))
#     while len(q) > 0:
#         g, u = hq.heappop(q)
#         if not visited[u]:
#             visited[u] = True
#             for w, v in G[u]:
#                 if not visited[v]:
#                     f = w + g
#                     if f < cost[v]:
#                         path[v] = u
#                         cost[v] = f
#                         hq.heappush(q, (f,v))
    
#     return path, cost
#endregion
#region BELLMANFORD
# def bellmannford(G, a):
#     n = len(G)
#     cost = [INF]*n
#     path = [-1]*n
#     cost[a] = 0
#     for _ in range(n-1):
#         for u in range(n):
#             for w, v in G[u]:
#                 f = cost[u] + w
#                 if f < cost[v]:
#                     cost[v] = f
#                     path[v] = u

#     for u in range(n):
#         for w, v in G[u]:
#             f = cost[u] + w
#             if f < cost[v]:
#                 return False, None, None

#     return True, path, cost
#endregion 
#region Algoritmo de prueba
# def find(s,a):
#   if s[a] < 0:
#     return a
#   grandpa = find(s, s[a])
#   return grandpa

# def union(s,a,b):
#   pa = find(s,a)
#   pb = find(s,b)
#   if pa == pb:
#     return
#   if s[pa] >= s[pb]:
#     s[pa] += s[pb]
#     s[pb] = pa
#   elif s[pb] > s[pa]:
#     s[pb] += s[pa]
#     s[pa] = pb

# def kruskal(q, n):
#   root = [-1]*n
#   T = []
#   while len(q):
#     ww, ii, ff = heappop(q)
#     if find(root, ii) != find(root, ff):
#       union(root, ii, ff)
#       T.append((ii, ff, ww))
#   return T

# def distance(a, b):
#   return sqrt(a**2 + b**2)

# def MCB(points):
#   n = len(points)
#   q = []
#   dist = [[0]*n for i in range(n)]

#   for u in range(n):
#     for v in range(u+1,n):
#       a = points[u][1] - points[v][1]
#       b = points[u][0] - points[v][0]
#       dist[u][v] = distance(a, b)
#       dist[v][u] = dist[u][v]
#       heappush(q, (dist[u][v], u, v))
  
  


#   mst = kruskal(q[:], n)
#   freq = [0]*n

#   for e in mst:
#     freq[e[0]] += 1
#     freq[e[1]] += 1
  
#   cycle = []
#   outPoints = []

#   for p in range(n):
#     if freq[p] == 1:
#       cycle.append(p)
#     else:
#       outPoints.append(p)
  
#   #print(cycle)
#   while len(outPoints):
    
#     m = len(cycle)
#     e = outPoints.pop()
#     idx = 0
    
#     for i in range(1, len(cycle)):
#       if dist[e][cycle[idx]] > dist[e][cycle[i]]:
#         idx = i
    
#     if dist[cycle[idx-1]][e] > dist[cycle[(idx+1)%m]][e]:
#       cycle.insert(idx, e)
#     else:
#       cycle.insert(idx+1, e)
#     #print(cycle)
  
#   return cycle

# # P = [(1,1),(2,2),(3,1),(1,5)]
# P = [
#   (1,4),
#   (2,2),
#   (3,1),
#   (3,3),
#   (3,4),
#   (4,1),
#   (4,4)
# ]
# tsp = MCB(P)
# print(tsp) 

#endregion
#region FORDFULKERSON
# def bfs(G, s, e):
#     n = len(G)
#     cam = []
#     visited = [False]*n
#     queued = [False]*n
#     queued[s] = True
#     q = [s]
#     while len(q) > 0:
#         u = q.pop()
#         if not visited[u]:
#             visited[u] = True
#             cam.append(u)
#             if u == e:
#                 break
#             for v, w in reversed(G[u]):
#                 if not queued[v] and w > 0:
#                     queued[v] = True
#                     q.append(v)
#     mini = INF
#     nun = len(cam)
#     for i in range(nun - 1):
#         for v, w in G[cam[i]]:
#             if v == cam[i+1] and w < mini:
#                 mini = w
#     return cam, mini if visited[e] else None

# def fordFulkerson(G, F):
#     while True:
#         c, mini = bfs(G, 0, 24) ## camino
#         if mini == None: ## condicion de parada
#             break
#         nun = len(c)
#         ## modifica el arrgelo flujo
#         for i in range(nun-1):
#             cont = -1
#             for v, w in F[c[i]]:
#                 cont += 1
#                 if v == c[i+1]:
#                     F[c[i]][cont] = (v, w + mini)
#         ## modifica el arreglo original
#         for i in range(nun-1):
#             cont = -1
#             for v, w in G[c[i]]:
#                 cont += 1
#                 if v == c[i+1]:
#                     G[c[i]][cont] = (v, w - mini) ## resta la capacidad
#                     cont = -1
#                     ## crea los arcos opuestos
#                     for u, w in G[v]:
#                         cont += 1
#                         if u == c[i]:
#                             G[v][cont] = (c[i], mini + w) ## si ese arco ya existia aumenta la capacidad
#                             cont = 24
#                     if cont != 24:
#                         G[v].append((c[i], mini)) ## si no existia lo crea
#     return F
#endregion
#region Algoritmo backup
# import math 
# INF = math.inf

# def DefinirPuntoInicioYFin(G):
#     n = len(G)
#     maxi = -1
#     pi = 0
#     pf = 0
#     for i in range(n):
#         for v, w in G[i]:
#             if w > maxi:
#                 maxi = w
#                 pi = i
#                 pf = v
#     return pi, pf 

# def Union(G, a, b):
#     G[b] = a

# def CheckHaveMin(G, s, path):
#     mini = INF
#     posFinal = -1
#     for v, w in G[s]:
#         if w < mini and (find(path, s) != find(path, v)):            
#             mini = w
#             posFinal = v
#     if posFinal != -1:
#         Union(path, s, posFinal)
#     return posFinal
    

# def UFDSModificado(G, s , e):
#     n = len(G)
#     path = [x for x in range(n)]
#     order = []
#     pos = s
#     order.append(pos)
#     for _ in range(n):
#         pos = CheckHaveMin(G, pos, path)
#         order.append(pos)
#     if pos == e:
#         return None
#     else:
#         order.append(s)
#         return order 
#endregion
