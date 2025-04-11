from kol2testy import runtests

def DFS_check(G):
    def DFS_Visit(G,u):
        visited[u]=True
        for v,_ in G[u]:
            if not visited[v]:
                DFS_Visit(G,v)
    n=len(G)
    visited=[False for v in range(n)]
    DFS_Visit(G,0)
    for v in visited:
        if not v:
            return False
    return True

def eadgelist(G):
    n=len(G)
    F=[]
    for u in range(n):
        for v,c in G[u]:
            F.append((c,u,v))
    F.sort()
    L=[]
    for i in range(0,len(F),2):
        L.append(F[i])
    
    return L

def lis_sas(L,n):
    G=[[] for _ in range(n)]
    for c,u,v in L:
        G[u].append((v,c))
        G[v].append((u,c))
    return G
            
def beautree(G):
    n=len(G)
    L=eadgelist(G)
    i=0
    while i<len(L)-n+2:
        t=L[i:i+n-1]
        g=lis_sas(t,n)
        if DFS_check(g):
            suma=0
            for e in t:
                suma+=e[0]
            return suma
        i+=1
    return None
                


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)