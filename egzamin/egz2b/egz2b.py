from egz2btesty import runtests
from queue import PriorityQueue

'''
Karolina Nitsch 421767
Z podanej listy krawędzi tworzę listę sąsiedztwa (zamieniam typ 'I' na 0, a 'P' na 1 co ulatwia pozniej zapisywanie odleglosci)  
i uruchamiam zmodyfikowany algorytm Dijkstry, w ktorym osobno licze odleglosci jezeli pociag dojezdza do danej stacji linia indyjska i osobno jezeli dojezdza linia przyladkowa. 
Dzięki temu algorytm jest poprawny i nie gubi danych.
Dodatkowo uwzgledniam czas przejazdu przez dworzec w zaleznosci od rozstawu szyn ktorymi wjezdza i ktorymi wyjezdza. 
Zlozonosc czasowa algorytmu wynosi O(mlogm) 
'''

def lista_sasiedztwa(G):
  n = max(max(u, v) for u, v, _, _ in G) + 1
  lista=[[] for _ in range (n)]
  for el in G:
    u,v,d,typ=el
    nr=0
    if typ=='P':
      nr=1
    lista[u].append((v,d,nr))
    lista[v].append((u,d,nr))
  return lista


def Dijkstra(G,s):
  n=len(G)
  d=[[float('inf'),float('inf')] for _ in range(n)]
  pq=PriorityQueue()
  d[s]=[0,0]
  for sasiad in G[s]:
    v, x, typ2 = sasiad
    if d[v][typ2] > x:
        d[v][typ2] = x
        pq.put((d[v][typ2], v, typ2))

  while not pq.empty():
      odl,u,typ=pq.get()


      for sasiad in G[u]:
        v,x,typ2=sasiad

        if typ2==typ==0:
            if d[v][typ2]>odl+x+5:
              d[v][typ2] = odl + x+5
              pq.put((d[v][typ2],v,typ2))
        elif typ2==typ==1:
            if d[v][typ2]>odl+x+10:
              d[v][typ2] = odl + x+10
              pq.put((d[v][typ2],v,typ2))

        else:
          if d[v][typ2] > odl + x + 20:
            d[v][typ2] = odl + x + 20
            pq.put((d[v][typ2], v, typ2))


  return d
def tory_amos( E, A, B ):
  # tu prosze wpisac wlasna implementacje
  G=lista_sasiedztwa(E)
  d=Dijkstra(G,A)
  return min(d[B])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
