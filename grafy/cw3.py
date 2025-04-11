# Algorytm Dijkstry dla reprezentacji macierzowej
#Algorytm Bellmana-Forda dla reprezentacji listowej
#algorytm wypisujacy najkrotsza sciezke do zad. wierzcholka npst. tablicy parent
#alg. znajdujacy najkrotsze sciezki z zad. wierzcholka w DAG
#alg. znajdujacy sciezke z s do t o minimalnym iloczynie wag krawedzi -zamienic wagi na ich logarytmy (suma logarytmow to logarytm iloczynu, a logarytm jest funkcja rosnaca) i wykonac algorytm Dijkstry
#krawedzie maja wagi ze zbioru {1,...|E|}, parami różne. szukamy najkrotszej sciezki z s do t, malejące krawędzie
# Alicja i Bob jadą z miasta s do t, zmieniaja sie na kazdym odcinku. znalezc trase,taka zeby alicja przejechala jak najmniej. (zaczyna alicja)
# miasta, krawedzie o okreslonych wagach - drogi i ich długosc w km, samochod spala 1l na 1km. w miastach podana jest cena paliwa. jedziemy z s do t. rozwiazanie wielomianowe. d=8 pojemnosc baku

def Dijkstra(M,s):
    n=len(M)
    d=[float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    d[s]=0
    while True:
        tmp=float('inf')
        u=float('inf')
        for c in range(n):
            if d[c]<tmp and not visited[c]:
                tmp=d[c]
                u=c
        if u==float('inf'):
                break
        visited[u]=True
        for i in range(n):
            if M[u][i]<float('inf'):
                if d[i]>d[u]+M[u][i]:
                    d[i]=d[u]+M[u][i]
                    parent[i]=u
        return d, parent
        

from queue import PriorityQueue
def prim(G,v):
    n=len(G)
    pq=PriorityQueue()
    pq.put((0,v))
    d=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    vis=[False for _ in range(n)]
    d[0]=0
    while not pq.empty():
        costam,t=pq.get()
        if not vis[t]:
            vis[t]=True
            for u,w in G[t]:
                if not vis[u]:
                    if d[u]>=w:
                        d[u]=w
                        parent[u]=t
                        pq.put((d[u],u))
    suma=0
    for i in range(n):
        suma+=d[i]

    return parent,suma

def find(x,parent):
    if parent[x]!=x:
        parent[x]=find(parent[x],parent)
    return parent[x]

def union(x,y,parent,rank):
    x=find(x,parent)
    y=find(y,parent)
    if x==y: return
    if rank[x]>rank[y]:
        parent[y]=x
    else:
        parent[x]=y
        if rank[x]==rank[y]:
            rank[y]+=1

def kruskal(G,n):
    G.sort(key=lambda x: x[2])
    parent=[i for i in range(n)]
    rank=[0 for _ in range(n)]
    A=[]
    for e in G:
        u,v,c=e
        if find(u,parent)!=find(v,parent):
            union(u,v,parent,rank)
            A.append(e)
    return A

G=[(0,1,2),(0,4,10),(0,3,5),(1,2,1),(1,4,5),(2,3,20),(3,4,20)]
print(kruskal(G,5))

def lista_sasiedztwa(G):
  n = max(max(u, v) for u, v, _ in G) + 1
  lista=[[] for _ in range (n)]
  for el in G:
    u,v,w=el
    lista[u].append((v,w))
    lista[v].append((u,w))
  return lista

G=lista_sasiedztwa(G)
print(prim(G,0))

def hamilton_path(G):
    def DFS_Visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit(G,v)
        path.append(u)
    n=len(G)
    path=[]
    visited=[False for v in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    path.reverse()
    for i in range(n-1):
        if not path[i+1] in G[path[i]]:
            return False
    return path

G=[[1,2,5],[3],[],[2,4],[2],[3,4]]
print(hamilton_path(G))

def goodstart(G):
    def DFS_Visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                DFS_Visit(G,v)
        path.append(u)
    n=len(G)
    path=[]
    visited=[False for v in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u)
    path.reverse()
    visited=[False for v in range(n)]
    u=path[0]
    path=[]
    DFS_Visit(G,u)
    if len(path)!=n:
        return False
    return u

print(goodstart(G))

from math import ceil

def guide(G,A,B,K):
  G=lista_sasiedztwa(G)
  n=len(G)
  d=[0 for _ in range(n)]
  pq=PriorityQueue()
  d[A]=K
  pq.put((-K,A))

  while not pq.empty():
      poj,u=pq.get()
      poj*=-1
      for sasiad in G[u]:
        v,x=sasiad
        if d[v]<min(poj,x):
            d[v]=min(poj,x)
            pq.put((-d[v],v))
  return ceil(K/d[B])

def alicja_bob(G,x,y):
  n=len(G)
  d=[[float('inf'),float('inf')] for _ in range(n)]
  pq=PriorityQueue()
  d[x]=[0,0]
  pq.put((0,x,0))
  pq.put((0,x,1))

  while not pq.empty():
      odl,u,os=pq.get()
      for sasiad in G[u]:
        v,x=sasiad
        if os==0:
            if d[v][1]>odl+x:
                d[v][1]=odl+x
                pq.put((d[v][1],v,1))
        else:
            if d[v][0]>odl:
                d[v][0]=odl
                pq.put((d[v][0],v,0))
  return min(d[y])



E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10),
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

E = lista_sasiedztwa(E)

print(alicja_bob(E,9,2))

def petrol(G,a,b,D,costs):
      n=len(G)
      d=[[float('inf') for _ in range(D+1)] for _ in range(n)]
      parent=[[(None,None) for _ in range(D+1)] for _ in range(n)]
      pq=PriorityQueue()
      for i in range(D+1):
          d[a][i]=i*costs[a]
          pq.put((d[a][i],a,i))

      while not pq.empty():
          odl,u,fuel=pq.get()
          for sasiad in G[u]:
            v,x=sasiad
            c=-costs[u]
            for f in range(fuel,D+1):
              c+=costs[u]
              if d[u][f]>d[u][fuel]+c:
                  d[u][f] = d[u][fuel] + c
                  parent[u][f]=(u,fuel)
                  pq.put((d[u][f],u,f))
            if x<=fuel:
                if d[v][fuel-x]>d[u][fuel]:
                    parent[v][fuel-x]=(u,fuel)
                    d[v][fuel-x]=d[u][fuel]
                    pq.put((d[v][fuel-x],v,fuel-x))
      path=[]
      y=b
      f=0
      while (y,f)!=(None,None):
          path.append((y,f))
          y,f=parent[y][f]
      path.reverse()
      return path, d[b][0]

G=[[(1,1),(5,3),(4,2)],[(2,5),(0,1),(4,8)],[(1,5),(4,10),(3,11)],[(2,11),(7,10)],[(1,8),(2,10),(0,2)],[(0,3),(6,15)],[(5,15),(7,9)],[(3,10),(6,7)]]

costs=[2,3,4,1,7,8,1,1]
print(petrol(G,0,3,15,costs))

def mal_kraw(G,s,t):
  n=len(G)
  d=[float('inf') for _ in range(n)]
  pq=PriorityQueue()
  d[s]=0
  pq.put((0,s,float('inf')))

  while not pq.empty():
      odl,u,last=pq.get()
      if u==t:
          return d[t]
      for sasiad in G[u]:
        v,x=sasiad
        if x<last:
            d[v]=min(d[v],odl+x)
            pq.put((odl+x,v,x))
  return d[t]


E = [(0, 1, 15), (0, 2, 2), (0, 3, 6), (1, 2, 14), (1, 4, 7), (2, 5, 3), (2, 6, 4), (3, 7, 2),
         (4, 8, 6), (5, 9, 2), (6, 8, 5), (7, 9, 8), (8, 10, 5), (9, 10, 1)]

s = 0
t = 10

G=lista_sasiedztwa(E)

print(mal_kraw(G,s,t))

def wyscigi(G):
    def DFS_Visit(G,u,cnt):
        nonlocal time
        visited[u]=True
        cnt+=1
        for v in G[u]:
            if not visited[v]:
                cnt=max(cnt,DFS_Visit(G,v,cnt))
        czasy_przetw[u]=time
        time+=1
        print(cnt)
        return cnt

    time=0
    n=len(G)
    czasy_przetw=[0 for _ in range(n)]
    visited=[False for v in range(n)]
    for u in range(n):
        if not visited[u]:
            DFS_Visit(G,u,0)
    newG=[[] for _ in range(n)]
    czasy=czasy_przetw.copy()
    for i in range(n):
        for j in G[i]:
            newG[j].append(i)
        czasy[i]=(czasy[i],i)
    czasy.sort(reverse=True)
    visited=[False for v in range(n)]
    for czas,u in czasy:
        if not visited[u]:
            cnt=DFS_Visit(newG,u,0)
            if cnt==1:
                return False
    return True

print('\n')

G=[[1,4],[2],[0,6],[4,5],[6],[4,3],[5,7],[5]]
print(wyscigi(G))