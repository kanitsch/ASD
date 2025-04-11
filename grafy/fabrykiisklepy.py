from collections import deque

def BFS(G,s,t):
    n=len(G)
    vis=[False for _ in range(n)]
    par=[None for _ in range(n)]
    vis[s]=True
    Q=deque()
    Q.append(s)
    while Q:
        u=Q.popleft()
        for v in range(n):
            if G[u][v] and not vis[v]:
                vis[v]=True
                par[v]=u
                if v==t:
                    T=[]
                    p=t
                    while p!=None:
                        T.append(p)
                        p=par[p]
                    T.reverse()
                    return T
                Q.append(v)
    return []

def ff(G,s,t):
    flow=0
    path=BFS(G,s,t)
    if not path:
        return None
    while path:
        n=len(path)
        min_cap = G[path[0]][path[1]]
        for i in range(1, n - 1):
            min_cap = min(min_cap, G[path[i]][path[i + 1]])
        flow+=min_cap
        for i in range(n - 1):
            G[path[i]][path[i + 1]] -= min_cap
            G[path[i + 1]][path[i]] += min_cap
        path=BFS(G,s,t)

    return flow

def sprawdz(G,S,T):
    n=len(G)
    newG=[[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            newG[i][j]=G[i][j]
    for s,p in S:
        newG[n][s]=p
    suma=0
    for t,q in T:
        newG[t][n+1]=q
        suma+=q
    if ff(newG,n,n+1)==suma:
        return True
    return False

G=[[0,7,0,3,0,0,0],
   [0,0,0,4,6,0,0],
   [9,0,0,0,0,9,0],
   [0,0,0,0,9,0,0],
   [0,0,0,0,0,0,0],
   [0,0,0,3,0,0,0],
   [0,0,0,0,8,0,0]]

S=[(0,10),(2,12),(6,8)]
T=[(1,3),(3,10),(4,2),(5,5)]



print(sprawdz(G,S,T))

G=[[0,1,0,1],
   [1,0,0,1],
   [0,0,0,1],
   [1,1,1,0]]
print(ff(G,3,1))
