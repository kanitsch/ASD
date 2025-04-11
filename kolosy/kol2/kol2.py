from kol2testy import runtests
from queue import PriorityQueue

def lista_sasiedztwa(G):
  n = max(max(u, v) for u, v, _ in G) + 1
  lista=[[] for _ in range (n)]
  for el in G:
    u,v,w=el
    lista[u].append((v,w))
    lista[v].append((u,w))
  return lista

def warrior( G, s, t):
  # tu prosze wpisac wlasna implementacje
  G=lista_sasiedztwa(G)
  n=len(G)
  q=PriorityQueue()
  d=[[float('inf') for _ in range(17)] for _ in range(n)]
  d[s][16]=0
  q.put((0,s,16))
  while not q.empty():
    dist, u, rest = q.get()
    if u==t:   return dist
    for (v,w) in G[u]:
        if rest>=w:
            if d[v][rest-w]>dist+w: 
                d[v][rest-w]=dist+w
                q.put((d[v][rest-w],v,rest-w))
        if d[v][16-w]>dist+w+8:
            d[v][16-w]=dist+w+8
            q.put((dist+w+8,v,16-w))
  
  return -1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
