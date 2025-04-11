from zad6testy import runtests
from collections import deque

def bfs(G,s,t):
    Q=deque()
    Q.append(s)
    vis=[False for _ in range(len(G))]
    par=[None for _ in range(len(G))]
    while Q:
        u=Q.popleft()
        vis[u]=True
        if u==t:
            break
        for v in G[u]:
            if not vis[v]:
                Q.append(v)
                par[v]=u
    if not vis[t]:
        return None
    v=t
    path=[]
    while v!=None:
        path.append(v)
        v=par[v]
    return path

def powrot(G,path):
    n=len(path)
    for i in range(n-1):
        G[path[i]].append(path[i+1])
        G[path[i+1]].remove(path[i])
    return G

def binworker( M ):
    n=len(M)
    G=[[] for _ in range(2*n+2)]
    for u in range(n):
        for v in M[u]:
            G[u].append(v+n)
        G[2*n].append(u)
        G[u+n].append(2*n+1)
    res=0
    while path:=bfs(G,2*n,2*n+1):
        G=powrot(G,path)
        res+=1
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )

