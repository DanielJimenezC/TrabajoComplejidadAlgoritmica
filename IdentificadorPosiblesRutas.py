def identificarRutas(G, v, visited, q):    
    q.append(v)
    option = []
    for nodos in G[v]:
        if(visited[nodos] == False):
            option.append(nodos)
    print(q)
    visited[v] = True
    if all(nodo == True for nodo in visited):
        print(visited)
    for nodos in option:
        if(visited[nodos] == False):                        
            if(identificarRutas(G, nodos, visited,q) == True):
                break
            else:
                print(visited)



G = [
[4,2,1],
[0,2,4],
[1],
[4,2],
[0,1,3,2]
]
n = len(G)

identificarRutas(G, 4, [False]*n,[])
