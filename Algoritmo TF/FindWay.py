import Math

def bellmannford(G, a):
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

def Way(path, d):
    road = []
    if path[d] != -1:
        way(path, path[d])
    road.append(d)

def FoundWay(G,s):
    n = len(G)
    find, path, cost = bellmanford(G, s)
    m = cost[0]
    destino = s
    for i in range(1,n):
        if m < cost[i]:
            m = cost[i]
            destino = i
    if find:
        Road = Way(path, destino)
    return Road


    

G = []
with open('grafito-prim.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i*2], nums[i*2+1]))

print(bellmannford(G,2))