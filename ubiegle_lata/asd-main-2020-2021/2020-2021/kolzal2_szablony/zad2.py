from zad2testy import runtests
def order(L, k):
    def DFS_Visit(G,u):
        visited[u[1]]=True
        for v in G[u[0]%10**k]:
            if not visited[v[1]]:
                DFS_Visit(G,v)
        path.insert(0,u[0])
    n=len(L)
    path=[]
    visited=[False for v in range(n)]
    divs=[[] for _ in range(10**k)]
    for i in range(n):
        if L[i]//10**k >= 10**k:
            continue
        divs[L[i]//10**k].append((L[i],i))
    for u in range(n):
        if not visited[u]:
            DFS_Visit(divs,(L[u],u))
    for i in range(n-1):
        if path[i+1]//10**k!=path[i]%10**k:
            return None

    return path


runtests( order )

