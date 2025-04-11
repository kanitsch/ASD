from zad8testy import runtests
from math import ceil, sqrt

# program dziala, pewnie jest nieoptymalny, ale chyba poprawny. sortuje krawedzie i w petli usuwam w kazdej iteracji najmniejsza krawedz i wykonuje algorytm kruskala,
#porownujac roznice najwiekszej i najmniejszej krawedzi z dotychczasowym najlepszym wynikiem

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
    G.sort(key=lambda x: x[2])
    V=[Node(i) for i in range(n)]
    A=[]
    for e in G:
        u,v,c=e
        if find(V[u])!=find(V[v]):
            union(V[u],V[v])
            A.append(e)
    if len(A)==n-1:
        return A
    return [(0,0,float('inf'))]
    

def highway( A ):
    # tu prosze wpisac wlasna implementacje
    n=len(A)
    kraw=[]
    for i in range(n-1):
        for j in range(i,n):
            dist=ceil(sqrt((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2))
            kraw.append((i,j,dist))
    res=float('inf')
    kraw.sort(key=lambda x: x[2])
    for j in range(len(kraw)-n+1 ):
        tab=kraw[j:]
        tab=kruskal(tab,n)[-1][2]
        if tab ==float('inf'):
            break
        res=min(res,tab-kraw[j][2])

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )