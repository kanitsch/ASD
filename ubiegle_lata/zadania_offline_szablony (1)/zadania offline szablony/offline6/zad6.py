from zad6testy import runtests
from collections import deque

def longer( G, s, t ):
    def bfs(G,s):
        n=len(G)
        Q=deque()
        vis=[False for _ in range(n)]
        vis[s]=True
        d=[float('inf') for _ in range(n)]
        par=[None for _ in range(n)]
        d[s]=0
        Q.append(s)
        while Q:
            u=Q.popleft()
            for v in G[u]:
                if not vis[v]:
                    vis[v]=True
                    d[v]=d[u]+1
                    par[v]=u
                    Q.append(v)
        return vis, par, d
    vis,par,d=bfs(G,s)
    if not vis[t]:
        return None
    v=t
    while v!=s:
        G[par[v]].remove(v)
        G[v].remove(par[v])
        vis2,par2,d2=bfs(G,s)
        if d2[t]>d[t]:
            return (par[v],v)
        G[par[v]].append(v)
        G[v].append(par[v])
        v=par[v]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )