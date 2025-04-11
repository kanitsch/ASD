from egzP1btesty import runtests 
from queue import PriorityQueue


def sasiedztwa(G):
    n=len(G)
    lista=[[] for _ in range(n)]
    for el in G:
        u,v,d=el
        lista[u].append((v,d))
        lista[v].append((u,d))
    return lista    


def turysta( G, D, L ):
    n=len(G)
    G=sasiedztwa(G)
    pq=PriorityQueue()
    d=[[float('inf') for _ in range(3)]for _ in range(n)]
    d[D]=[0,0,0]
    pq.put((0,D,-1))
    mini=float('inf')
    while not pq.empty():
        costam=pq.get()
        de,u,ile_odw=costam
        for v in G[u]:
            sasiad,l=v
            if ile_odw==2 and sasiad==L:
                mini=min(mini,d[u][ile_odw]+l)
            if ile_odw<2 and sasiad!=D and sasiad!=L:    
                if d[sasiad][ile_odw+1]>d[u][ile_odw]+l:
                    d[sasiad][ile_odw+1]=d[u][ile_odw]+l
                    pq.put((d[sasiad][ile_odw+1],sasiad,ile_odw+1))
    
    
    return mini

runtests ( turysta )