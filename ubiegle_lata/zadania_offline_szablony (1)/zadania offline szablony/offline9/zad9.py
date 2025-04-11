from zad9testy import runtests
from collections import deque
from copy import deepcopy

def BFS(G,s,t1,t2):
    n=len(G)

    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]

    vis[s]=True
    Q=deque()
    Q.append(s)

    while len(Q)>0:
        u=Q.popleft()
        for v in range(n):
            if G[u][v] and not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t1 or v==t2:
                    T=[]
                    p=v
                    while p!=None:
                        T.append(p)
                        p=par[p]
                    return T[::-1]
                Q.append(v)
    return []

def cap(G,path):
    n=len(path)
    min_cap=G[path[0]][path[1]]
    for i in range(1,n-1):
        min_cap=min(min_cap,G[path[i]][path[i+1]])
    return min_cap

def modify(G,path,min_cap):
    n=len(path)
    for i in range(n-1):
        G[path[i]][path[i+1]]-=min_cap
        G[path[i+1]][path[i]]+=min_cap

def ff(G,s,t1,t2):
    n=len(G)
    flow=0

    path=BFS(G,s,t1,t2)
    if len(path)==0:
        return 0

    while len(path)>1:
        min_cap=cap(G,path)
        flow+=min_cap
        modify(G,path,min_cap)
        path=BFS(G,s,t1,t2)

    return flow

def matrix(G):
    n=max(max(G[i][0],G[i][1]) for i in range(len(G)))
    M=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for u,v,p in G:
        M[u][v]=p
    return n, M


def maxflow( G,s ):
    # tu prosze wpisac wlasna implementacje
    n, M=matrix(G)
    G=deepcopy(M)
    maxx=0
    for i in range(n-1):
        if i!=s:
            for j in range(i+1,n):
                if j!=s:
                    maxx=max(maxx,ff(G,s,i,j))
                    G=deepcopy(M)
    return maxx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True)