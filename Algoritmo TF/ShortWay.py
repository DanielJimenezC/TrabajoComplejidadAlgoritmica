import math
import heapq as pq

def Road(visited, start):
    found = False
    n = len(visited)
    for i in range(n):
        if i != start:
            if visited[i] == True:
                found = True
            else:
                found = False
                return found
        else:
            found = True
    return found

def ShortWay(G, start):
    n = len(G)
    path = [-1]*(n+1)
    queue = []
    visited = [False]*n
    path[0] = start
    index = 1
    for nodo, weight in G[start]:
        pq.heappush(queue,(nodo,weight))
    while len(queue) > 0:
        cost = math.inf
        small = 0
        for _ in range(len(queue)):
            v, w = pq.heappop(queue)
            if not visited[v]:
                if w < cost:
                    small = v
                    cost = w
                    path[index] = v 
            if len(queue) == 0:
                break
        visited[small] = True
        index += 1
        if Road(visited, start):
            for n, _ in G[small]:
                if n == start: 
                    path[index] = start
                    return path, True
                else:
                    return path, False
        for n, p in G[small]:
            if n != start:
                pq.heappush(queue, (n,p))

def ShowRoad(G, start):
    Road, Found = ShortWay(G, start)
    if Found:
        print("LA RUTA ES: ")
        for i in range(len(Road)):
            print(Road[i])
    else:
        print("no hay camino")

G = []
with open('grafito.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i*2], nums[i*2+1]))

ShowRoad(G, 0)
    



