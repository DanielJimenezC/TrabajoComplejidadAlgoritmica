def prim(distancia,nombre):
    n = len(distancia)
    dist = [math.inf]*n
    path = [None]*n
    visited = [False]*n
    q = []
    hq.heappush(q, (0, 0))
    contador=0
    while len(q) > 0:
        print(contador)
        contador+=1
        _, u = hq.heappop(q)
        if not visited[u]:
            visited[u] = True
            for v, w in distancia[u]:
                if not visited[v] and w < dist[v] and w!=0 :
                    dist[v] = w
                    path[v] = nombre[v][u]
                    hq.heappush(q, (w, v))
    print(path)