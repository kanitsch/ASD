from kol2testy import runtests

class Node:
    def __init__(self,value):
        self.val=value
        self.parent=self
        self.rank=0
        
def find(x):
    if x.parent!=x:
        x.parent=find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
            
def kruskal(G,n):
    V=[Node(i) for i in range(n)]
    A=[]
    for e in G:
        c,u,v,i=e
        if find(V[u])!=find(V[v]):
            union(V[u],V[v])
            A.append(e)
    if len(A)<n-1:
        return None
    return A

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
    
    for i in range(len(L)):
        c,u,v=L[i]
        L[i]=(c,u,v,i)
    return L
            
def beautree(G):
    n=len(G)
    L=eadgelist(G)
    i=0
    while i<len(L)-n+2:
        t=L[i:]
        A=kruskal(t,n)
        if A and A[-1][3]-A[0][3]==n-2:
            suma=0
            for c,u,v,i in A:
                suma+=c
            return suma
        if not A:
            return None
        i=A[-1][3]-n+2
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True)
