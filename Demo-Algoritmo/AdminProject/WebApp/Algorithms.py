#Algoritmo PRIM
import heapq as hq
import math
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




def prim(G):
    n = len(G)
    visited = [False]*n
    path = [-1]*n
    cost = [INF]*n
    queue = []
    s = 0
    cost[s] = 0
    hq.heappush(queue,(0,s))
    while len(queue) > 0:
        _, u = hq.heappop(queue)
        if not visited[u]:
            visited[u] = True
            for v, w in G[u]:
                if not visited[v] and w < cost[v]:
                    path[v] = u
                    cost[v] = w
                    hq.heappush(queue, (w, v))

    return path, cost

