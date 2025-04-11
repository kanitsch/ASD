'''
Karolina Nitsch
Przeksztalcam liste krawedzi na liste sasiedztwa, a liste rowerow tak, aby dla kazdego wierzcholka byla wypisana najmniejsza wartosc p/q w tym wierzcholku,
(tylko jezeli p/q jest mniejsze niż 1, inaczej się nie opłaca jechać rowerem)
lub 0 jesli nie ma tam roweru. Dla kazdego wierzcholka uruchamiam algorytm Dijkstry i zapisuję wyniki w tablicy d.
Następnie dla każdego wierzchołka i, jeżeli jest w nim rower, obliczam sumę dobiegnięcia do tego wierzchołka z wierzchołka s oraz dojechania z i do t rowerem
Złożoność szacuję na O(VElogV)

teraz jest dijkstra od s i od t zamiast tego i jest O(ElogV) 
'''

from egz1atesty import runtests
from queue import PriorityQueue

def lista_sasiedztwa(G):
  n=len(G)
  lista=[[] for _ in range(n)]
  for krawedz in G:
    u,v,w=krawedz
    lista[u].append((v,w))
    lista[v].append((u,w))
  return lista

def rowery(B,n):
  bicyckles=[None for _ in range(n)]
  for rower in B:
    i,p,q=rower
    if p/q>=1:
      continue
    if not bicyckles[i]:
      bicyckles[i]=(p/q)
    else:
      bicyckles[i]=min(bicyckles[i],p/q)
  return bicyckles
def Dijkstra(G,s):
  n=len(G)
  d=[float('inf') for _ in range(n)]
  pq=PriorityQueue()
  d[s]=0
  pq.put((0,s))
      
  while not pq.empty():
      odl,u=pq.get()
      for sasiad in G[u]:
        v,x=sasiad
        if d[v]>odl+x:
            d[v]=odl+x
            pq.put((d[v],v))
  return d

        
def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje
  n=len(G)

  B=rowery(B,n)
  G=lista_sasiedztwa(G)
  d1=Dijkstra(G,s)
  d2=Dijkstra(G,t)
  mini=d1[t]
  for i in range(n):
    if B[i]:
      droga=d1[i]+d2[i]*B[i]
      mini=min(mini,droga)
    
     

  return int(mini)       
    
    


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
