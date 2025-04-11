def DFS(G):
    def DFS_Visit(G,u):
        nonlocal time
        time+=1
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                DFS_Visit(G,v)
        time+=1
    time=0
    n=len(G)
    visited=[False for v in range(n)]
    parent=[None for v in range (n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    print(visited, '\n', parent)
    
L=[[1,5,3],[4,3],[],[2],[],[],[7,8],[8],[]]
DFS(L)

def topsort(G):
    def DFS_Visit(G,u,a):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit(G,v,a)
        a.append(u)
    a=[]
    n=len(G)
    visited=[False for v in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u,a)
    a.reverse()
    return a
            
def is_connected(G):
    n = len(G)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
    dfs(0)
    for u in range(n):
        if not visited[u]:
            return False

    return True

def euler(G):

    if not is_connected(G):
        return None

    n = len(G)
    for u in range(n):
        if len(G[u]) % 2 != 0:
            return None

    cycle = []

    def DFS_Visit(G, u):
        for v in G[u]:
            if not edges[u][v]:
                edges[u][v]=True
                edges[v][u]=True
                DFS_Visit(G, v)
        cycle.append(u)
    edges=[[False for _ in range(n)] for _ in range(n)]
    DFS_Visit(G, 0)
    cycle.reverse()
    return cycle


G=[[1,2,3,4],[0,2],[0,1,3,4],[0,2],[0,2]]
polos=[[1,3,4,9],[0,2],[1,3],[0,2],[0,5,6,7,8,9],[4,6],[4,5],[4,8],[4,7],[0,4]]
    
print(topsort(L))
print(euler(polos))
print(euler(G))
