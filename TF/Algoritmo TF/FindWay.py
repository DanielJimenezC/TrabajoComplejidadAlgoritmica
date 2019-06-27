import math
from time import time

def bellmanford(G, a):
    n = len(G)
    cost = [math.inf]*n
    path = [-1]*n
    cost[a] = 0
    for _ in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                f = cost[u] + w
                if f < cost[v]:
                    cost[v] = f
                    path[v] = u

    for u in range(n):
        for v, w in G[u]:
            f = cost[u] + w
            if f < cost[v]:
                return False, None, None

    return True, path, cost

def Way(path, d, road):
    if path[d] != -1:
        Way(path, path[d], road)
    road.append(d)
    return road

def FoundWay(G,s):
    n = len(G)
    find, path, _ = bellmanford(G, s)
    Road = []
    aux = []
    mayor = 0

    if find:
        for i in range(n):
            road = []
            aux = Way(path, i, road)
            if len(aux) > mayor:
                mayor = len(aux)
                Road = aux
        return Road
    else:
        return Road

G = []
with open('grafito.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i*2], nums[i*2+1]))

print(FoundWay(G, 0))