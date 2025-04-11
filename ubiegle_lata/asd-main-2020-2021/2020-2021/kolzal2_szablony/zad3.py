from zad3testy import runtests
from queue import  PriorityQueue

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


def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    d1=Dijkstra(G,s)
    d2=Dijkstra(G,t)
    if d1[t]==float('inf'):
        return 0
    n = len(G)
    visited = [False for v in range(n)]
    cnt=0
    def DFS_Visit(G,u):
        nonlocal cnt
        visited[u]=True
        for v,w in G[u]:
            if d1[u]+d2[u]==d1[v]+d2[v]==d1[t]==d1[u]+w+d2[v]:
                cnt+=1
            if not visited[v]:
                DFS_Visit(G,v)

    DFS_Visit(G,s)

    return cnt

    
runtests( paths )


